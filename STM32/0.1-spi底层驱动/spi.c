#include "reg.h"

/****************GPIO init*************************
		af gpioA 4 5 6 7 as NSS SCK MISO MOSI		 	

**************************************************/
void
Spi_Init(void){
	//RCC and SPI's bus init
	RCC_IOPAENR |= 1<<0;						/*	enable rcc&spi clock	*/
	RCC_APB2ENR |= 1<<12;						/*	enable rcc&spi clock	*/
	
	//GPIO_init
	GPIOA->MOR &= 0xFFFF00FF;					/*		choose the mode		*/
	GPIOA->MOR |= 0x0000BB00;					/*		as af mode,4567  	*/
	GPIOA->PPR |= 0x00005500;   				/*	pull-up port 4 5 6 7	*/
	GPIOA->OSR |= 0x0000CC00;					/*	port 5 7 at high speed	*/
	GPIOA->AFRL&= 0x00000000;					/*			AF0				*/

	//SPI_init
	SPI_REG->CR1 |= 0<<10; 						/*			mode			*/
	SPI_REG->CR1 |= 1<<9;
	SPI_REG->CR1 |= 1<<8;						/*			nss manage		*/
	SPI_REG->CR1 |= 1<<2;						/*	master selection		*/
	SPI_REG->CR1 |= 0<<11;						/*			8-bit frame		*/
	SPI_REG->CR1 |= 1<<1;						/*			CPOL-bit		*/
	SPI_REG->CR1 |= 1<<0;						/*			CPHA-bit		*/
	SPI_REG->CR1 |= 7<<3;						/*			Baud rate		*/
	SPI_REG->CR1 |= 1<<6;						/*			enable spi 		*/
}




/**********************************************************
			those functions only can be used after spi_init 

**********************************************************/
void
Spi_SetSpeed(u8 Speed){
	Speed &= 0x7;
	SPI_REG->CR1 &= 0xFFC7;
	SPI_REG->CR1 |= Speed<<3;
	SPI_REG->CR1 |= 1<<6;
}

u8
Spi_ReadWriteByte(u8 Data){
	u16 retrytimes = 0;
	while((SPI_REG->SR&1<<1)==0){
		retrytimes++;
		if (retrytimes>0xFFFE)return 0;
	}
	SPI_REG->DR = Data;
	retrytimes = 0;
	while((SPI_REG->SR&1<<0)==0){
		retrytimes++;
		if(retrytimes > 0xFFFE)return 0;
	}
	return SPI_REG->DR;
}

u16
Spi_ReadWriteHalfWord(u16 Data){
	u16 retrytimes = 0;											
	SPI_REG->CR1 &= 0<<6;									/*		disable spi	 	*/
	SPI_REG->CR1 |=	1<<11;									/*		16_bit mode		*/
	
	
	while((SPI_REG->SR&1<<1)==0){
		retrytimes++;
		if (retrytimes>0xFFFE)return 0;
	}
	SPI_REG->DR = Data;
	retrytimes = 0;
	while((SPI_REG->SR&1<<0)==0){
		retrytimes++;
		if(retrytimes > 0xFFFE)return 0;
	}
	return SPI_REG->DR;
}
