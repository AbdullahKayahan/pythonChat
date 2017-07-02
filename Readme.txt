*************************************************************************************************************************
*															*
*					BÝLGÝSAYAR AÐ TEKNOLOJÝLERÝ ÖDEV-1-						*
*						ABDULLAH KAYAHAN							*
*															*
*************************************************************************************************************************
*															*
*	Proje Dosyalarý: 												*
*		1- server.py: Server baðlantýsýnýn yapýldýðý dosyamýzdýr. Bu dosya bir port açarak dinlemeye baþlar.	*
*		     siniflar.py isimli dosyada bulunan Selection,Room ve User sýnýflarýný kullanarak multiple		*
*		     chat room'a izin verir.										*
*		2- siniflar.py: Server dosyasýnda kullanýlacak olan sýnýflarýn tanýmlandýðý dosyadýr. Asýl iþ bu 	*
*		     dosyadaki sýnýflar üzerinde dönmektedir. Menü iþlemleri, kullanýcý girisi, oda seçme ve benzeri 	*	
*		     iþlemler bu dosya üzerinde tanýmlanmýþtýr.								*
*		3- client.py:  Kullanýcýlarýn servera baðlanmak için kullanacaðý dosyadýr. Bu dosya çalýþtýrýlýrken	*
*		     hostname ve port numarasý parametre olarak verilmelidir.						*	
*	Dosyalarýn Çalýþtýrýlmasý:											*
*		server.py ---> terminal ekranýna "python server.py"  yazýlýp enter'a basýlmasý yeterlidir.		*
*		siniflar.py ---> bu dosyayý her hangi bir terminalde çalýþtýrmaya gerek yoktur. Bu dosya server.py 	*
*		 dosyasý içinden çaðrýlacaktýr.										*
*		client.py ---> Terminal Ekranýna "python client.py 127.0.0.1 5000" yazýlarak çalýþtýrýlmalýdýr.		*
*			Ardýndan menü ekraný kullanýcýya gösterilecektir. 						*
*			Giriþ yapmak için "<giris> kullanýcý_Adi sifre"  yazýlýp entera basýlýr.			*
*			Kayýt yapmak için "<kayit> kullanici_adi sifre"  yazýp entera basýlýr.				*
*			Chat odalarýný listelemek için "<listele>" yazýlýp entera basýlýr.				*
*			Bir odaya girmek için "<katil> oda_Adi" yazilip entera basýlýr.					*
*															*
*************************************************************************************************************************		
