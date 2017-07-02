# pythonChat

*************************************************************************************************************************
*															                                                                                          *
*					                                   BİLGİSAYAR AĞ TEKNOLOJİLERİ ÖDEV-1-	                            					*
*					                                          	ABDULLAH KAYAHAN		                                    					*
*															                                                                                          *
*************************************************************************************************************************
*															*
*	Proje Dosyaları: 												*
*		1- server.py: Server bağlantısının yapıldığı dosyamızdır. Bu dosya bir port açarak dinlemeye başlar.	*
*		     siniflar.py isimli dosyada bulunan Selection,Room ve User sınıflarını kullanarak multiple		*
*		     chat room'a izin verir.										*
*		2- siniflar.py: Server dosyasında kullanılacak olan sınıfların tanımlandığı dosyadır. Asıl iş bu 	*
*		     dosyadaki sınıflar üzerinde dönmektedir. Menü işlemleri, kullanıcı girisi, oda seçme ve benzeri 	*	
*		     işlemler bu dosya üzerinde tanımlanmıştır.								*
*		3- client.py:  Kullanıcıların servera bağlanmak için kullanacağı dosyadır. Bu dosya çalıştırılırken	*
*		     hostname ve port numarası parametre olarak verilmelidir.						*	
*	Dosyaların Çalıştırılması:											*
*		server.py ---> terminal ekranına "python server.py"  yazılıp enter'a basılması yeterlidir.		*
*		siniflar.py ---> bu dosyayı her hangi bir terminalde çalıştırmaya gerek yoktur. Bu dosya server.py 	*
*		 dosyası içinden çağrılacaktır.										*
*		client.py ---> Terminal Ekranına "python client.py 127.0.0.1 5000" yazılarak çalıştırılmalıdır.		*
*			Ardından menü ekranı kullanıcıya gösterilecektir. 						*
*			Giriş yapmak için "<giris> kullanıcı_Adi sifre"  yazılıp entera basılır.			*
*			Kayıt yapmak için "<kayit> kullanici_adi sifre"  yazıp entera basılır.				*
*			Chat odalarını listelemek için "<listele>" yazılıp entera basılır.				*
*			Bir odaya girmek için "<katil> oda_Adi" yazilip entera basılır.					*
*															*
*************************************************************************************************************************		
