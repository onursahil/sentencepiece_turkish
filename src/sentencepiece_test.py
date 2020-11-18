import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.Load("model_vocab/wiki-tr.model")
print("\n")
print(sp.EncodeAsPieces("Ağır hapis veya şeref ve haysiyete yönelik ve aynı zamanda Bankacılık mesleğinin esaslarıyla bağdaşmayan bir fiil ile mahkum edilmemiş olması"))
print('\n')
print(sp.EncodeAsPieces("Adaylar Banka ihtiyaçları doğrultusunda; nitelikleri göz önünde bulundurularak sürece alınırlar. Bu kriterler İnsan ve Kültür İş Birimi tarafından belirlenir ve Yönetim Kurulu’na onaya sunulur. "))
print('\n')
print(sp.EncodeAsPieces("İmza yetkisiz çalışanların işe alınma, yer değiştirme nakil ve görevde yükselme terfi işlemleri hakkında karar vermeye Genel Müdürlük yetkilidir."))
print('\n')
print(sp.EncodeAsPieces("Yönetici Adayları için Yön Yard.4’ten 3’e geçişte işe giriş tarihinden itibaren 1 yıl sayılır. (Sahada 6 ayda bir performans ölçümü yapıldığı için 2 dönem performans notu gerekir.)"))
print('\n')