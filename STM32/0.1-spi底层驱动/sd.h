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

/* SD???? */
#define CMD0    0       //???
#define CMD9    9       //??9 ,?CSD??
#define CMD10   10      //??10,?CID??
#define CMD12   12      //??12,??????
#define CMD16   16      //??16,??SectorSize ???0x00
#define CMD17   17      //??17,?sector
#define CMD18   18      //??18,?Multi sector
#define ACMD23  23      //??23,???sector???????N?block
#define CMD24   24      //??24,?sector
#define CMD25   25      //??25,?Multi sector
#define ACMD41  41      //??41,???0x00
#define CMD55   55      //??55,???0x01
#define CMD58   58      //??58,?OCR??
#define CMD59   59      //??59,??/??CRC,???0x00


u8 
Sd_init(void);

u8 
Sd_Enable(void);

u8 
Sd_Disable(void);

u8
Sd_SendCmd(u8 cmd, u32 arg, u8 crc);

