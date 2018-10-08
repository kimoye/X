import asyncio, aiomysql

#连接池建立函数后期再修改 部署的时候参数得改改
async def create_pool(loop, **kw):
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],                                        #数据库用户名
        password=kw['password'],                                #对应用户密码
        db=kw['db'],                                            #表名？maybe
        charset=kw.get('charset', 'utf8'),                      #字符集
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),                          #最大链接数
        minsize=kw.get('minsize', 1),                           #最小连接数
        loop=loop
    )

async def select(sql, args, size=None):
    global __pool

    #下面打开线程池pool，为异步操作
    #此处语法经深度学习后 改正 按道理with yeild from 等效于  with await
    #但是aiomysql官方sample以及PEP为 async with ，这的确更容易想通：上下文管理器嘛~
    #但是若是with await很矛盾他是什么东西 上下文管理器？

    async with __pool.acquire() as conn: 
        #DictCursor 字典形式的游标                       
        cur = await conn.cursor()
        await cur.excute(sql.replace('?','%s'), args or ())
        #输出信息
        print(cur.description)
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        #输出获取的列数
        print('rows returned: %s' % len(rs))
        return rs

async def execute(sql, args):
    print(sql)
    async with __pool as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
        except BaseException as e:
            raise  #待修改
        return affected

#***********************************************************#
#                  以上为数据库操作函数                       #
#                  以下为ORM的代码                           #
#***********************************************************#




####
class ModeMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == Model:
            print('skiping subclass')
            return type.__new__(cls, name, bases, attrs)
        
        tableName = attrs.get('__table__', None) or name
        print('found model %s', tableName)
        ####
        mappings   = dict()
        fields     = []
        primaryKey = None

        for k, v in attrs.items():
            if isinstance(v, Field):
                print('mapping %s --> %s' % (k, v))
                ###
                mappings[k] = v
                ###
                if v.primary_key:
                    if primaryKey is not None:
                        raise RuntimeError('two primary keys"\n" 1:%s"\n", 2:%s !!' % (primaryKey, k))
                    ##
                    primaryKey = k
                    
                else:
                    fields.append[k]
        if not primaryKey:
            raise RuntimeError('Primary key not found')
        
        ##
        for k in mappings.keys():
            attrs.pop(k)
        ##########将fields中的全部转化成字符而已
        escaped_fields = list(map(lambda f: "%s" % f, fields))
        attrs['__mappings__']           =   mappings
        attrs['__table']                =   tableName
        attrs['__primary_key__']        =   primaryKey
        attrs['__fields__']             =   fields


        ####
        ####
        attrs['__select__']     =   'select "%s", %s from "%s"' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__']     =   'insert into "%s" (%s, "%s") values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__']     =   'update "%s" set %s where "%s"=?' % (tableName, ', '.join(map(lambda f: '"%s"=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__']     =   'delete from "%s" where "%s"=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)


###############################################
#
#
#
###############################################

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'Model object has no attribute "%s"' % key)
    
    def __setattr__(self, key, value):
        self[key] = value
   
    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        ###
        if not getattr(self, key, None):
            field = self.__mappings__[key]
            if field.default:
                value = field.default if callable(field.default) else field.default
                ##
                print('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    
        