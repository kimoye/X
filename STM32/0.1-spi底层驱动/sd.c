#include "sd.h"

/********************SD  init***********************
	use Sd_init func when we connect to sdcard	 	

***************************************************/
u8 
Sd_init(void){
	u8 rdata, buff[6];						
	u16 i, retrytimes;
	
	
	Spi_Init();																/* 	spi init		*/
	
	Spi_SetSpeed(SPI_SPEED_LOW);											/*	low speed		*/

	for(i=0;i<0xf00;i++);													/*	delay	sometime*/
	for(i=0;i<10;i++){
		
		Spi_ReadWriteByte(0xff);											/*	80 premas(clks)	*/
	
	}
	
	retrytimes = 20;														/* reset SdCard		*/
	do{																		/*and pickup spimode*/
		rdata =	Sd_SendCmd(CMD0, 0, 0x95);
	}while((rdata!=0X01) && retrytimes--);
	if(retrytimes == 0)return 1;
	
	//get sd_infomation
	
}



u8 
Sd_Enable(void){
	u8 retrytimes = 0;
	GPIOA->PPR &= 0xFFFFFCFF;											/*pull-down gpioA p4*/
	GPIOA->PPR |= 0x10<<8;												/*configure	PUPDR	*/
	do{
		if(Spi_ReadWriteByte(0xFF)==0xFF)return 0;
		retrytimes ++;
	}while(retrytimes<0xFF);
	
	GPIOA->PPR &= 0xFFFFFCFF;											/*	pull-up gpioA p4*/
	GPIOA->PPR |= 0x01<<8;												/* 	this means fail	*/											
	return 1;															/* 	wait fail		*/
}




u8 
Sd_Disable(void){
	
	GPIOA->PPR &= 0xFFFFFCFF;											/*	pull-up gpioA p4	*/
	GPIOA->PPR |= 0x01<<8;												/* just cs disable		*/											
	return 0;															/* 	spi's cs line		*/
}

/*********************** Sd_SendCmd series functions ****************



********************************************************************/
u8
Sd_SendCmd(u8 cmd, u32 arg, u8 crc){
	u8 rdata;
	u8 retrytimes;
	Sd_Disable();
	if(Sd_Enable())return 0xFF;									/* enable cs again	 */
	
	//send cmd, according SD protocol, a cmd contain 6 bytes 
	//more detail ,see the books
	//we use spi protocol to contact with SD_Card, so we use lower spi driver
	Spi_ReadWriteByte(cmd|0x40);
	Spi_ReadWriteByte(arg>>24);
	Spi_ReadWriteByte(arg>>16);
	Spi_ReadWriteByte(arg>>8);
	Spi_ReadWriteByte(arg);
	Spi_ReadWriteByte(crc);
	
	//when we stop transfer
	if(cmd==CMD12){
		Spi_ReadWriteByte(0xFF);
	}
	retrytimes = 20;
	//get the status after sending a cmd
	do{
		rdata = Spi_ReadWriteByte(0xFF);
	}while((rdata&0x80)&&retrytimes--);
	
	return rdata;											/* return status code	*/
}

u8
SD_SendCommand_NoDeassert(u8 cmd, u32 arg,u8 crc)
{
	u8 rdata;
	u8 retrytimes = 0;
	Sd_Disable();do{
	if(Spi_ReadWriteByte(0xFF)==0xFF)return 0;
		retrytimes ++;
	}while(retrytimes<0xFF);
	Spi_ReadWriteByte(cmd|0x401);
	Spi_ReadWriteByte(arg>>24);
	Spi_ReadWriteByte(arg>>16);
	Spi_ReadWriteByte(arg>>8);
	Spi_ReadWriteByte(arg);
	Spi_ReadWriteByte(crc);
	
	//get respons
	retrytimes = 0;
	while((rdata=Spi_ReadWriteByte(0xFF))==0xFF){
		retrytimes ++;
		if(retrytimes>0xFE)break;
	}
	return rdata;
}

