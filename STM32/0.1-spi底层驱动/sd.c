#include "sd.h"
#include "spi.c"

u8 Sd_init(void){
	u16 i, retrytimes;
	u8 r1, buff[6];
	//spi init
	Spi1_Init();
	//
	Spi1_SetSpeed(SPI_SPEED_LOW);
	//delay
	for(i=0;i<0xf00;i++);
	//
	for(i=0;i<10;i++){
		//
		Spi_ReadWriteByte(0xff);
	
	}
	//
	retrytimes = 0;
	
	
}



void Sd_CsEnable(void){
	GPIOA->PPR &= 0xFFFFFFCF;
	GPIOA->PPR |= 0x10<<4;
}