#ifndef _SD_H
#define	_SD_H
#endif
#include "reg.h"
//sd tpye
#define SD_TYPE_MMC     0
#define SD_TYPE_V1      1
#define SD_TYPE_V2      2
#define SD_TYPE_V2HC    4
//spi speed
#define SPI_SPEED_LOW   0
#define SPI_SPEED_HIGH  1

// SD卡指令表 
#define CMD0    0       //卡复位
#define CMD9    9       //命令9 ，读CSD数据
#define CMD10   10      //命令10，读CID数据
#define CMD12   12      //命令12，停止数据传输
#define CMD16   16      //命令16，设置SectorSize 应返回0x00
#define CMD17   17      //命令17，读sector
#define CMD18   18      //命令18，读Multi sector
#define ACMD23  23      //命令23，设置多sector写入前预先擦除N个block
#define CMD24   24      //命令24，写sector
#define CMD25   25      //命令25，写Multi sector
#define ACMD41  41      //命令41，应返回0x00
#define CMD55   55      //命令55，应返回0x01
#define CMD58   58      //命令58，读OCR信息
#define CMD59   59      //命令59，使能/禁止CRC，应返回0x00


u8 
Sd_init(void);

u8 
Sd_Enable(void);

u8 
Sd_Disable(void);


/********发送命令失败会返回0xFF，可以利用这个判断发送成功与否
*********发送成功则返回响应码*****************************/
u8
Sd_SendCmd(u8 cmd, u32 arg, u8 crc);

u8
SD_SendCommand_NoDeassert(u8 cmd, u32 arg,u8 crc);

