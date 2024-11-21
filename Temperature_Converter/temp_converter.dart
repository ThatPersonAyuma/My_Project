import 'dart:io';
void main() {
  print("Selamat datang di converter suhu dalam satuan Celsius (C), Reaumur (R), Kelvin (K), dan Fahrenheit (F).");
  final satuan_awal=getSatuanAwal();
  final nilaiAwal=getNilaiAwal(satuan_awal);
  final satuanAkhir=getSatuanAkhir();
  final suhuAkhir=getNilai(satuan_awal,satuanAkhir,nilaiAwal);
  print("Suhu akhir yaitu $suhuAkhir°$satuanAkhir");
}

String getSatuanAwal(){
  while(true){
    stdout.write("Masukkan satuan awal: ");
    String? satuan_awal=stdin.readLineSync();
    try{
      satuan_awal=satuan_awal!.toUpperCase();
      if (['C', 'R', 'K', 'F'].contains(satuan_awal)){
        return satuan_awal;
      }
    } catch (e){
      print("Upss there is something wrong, $e");
    }
  }
}

String getSatuanAkhir(){
  while(true){
    stdout.write("Masukkan satuan akhir: ");
    String? satuan_awal=stdin.readLineSync();
    try{
      satuan_awal=satuan_awal!.toUpperCase();
      if (['C', 'R', 'K', 'F'].contains(satuan_awal)){
        return satuan_awal;
      }
    } catch (e){
      print("Upss there is something wrong, $e");
    }
  }
}

int getNilaiAwal(satuanAwal){
  while(true){
    stdout.write("Masukkan nilai dari suhu (dalam satuan °$satuanAwal): ");
    String? nilai=stdin.readLineSync();
    try{
      int nilaiAkhir=int.parse(nilai!);
      return nilaiAkhir;
    } on Exception{
      print("Something wrong.");
    }
  }
}
num getNilai(String satuanAwal, String satuanAkhir, int suhuAwal){
  Map dataBatasSuhu={
    'C': [0,100,100],
    'R': [0,80,80],
    'K': [273,373,100],
    'F': [32,212,180]
  };
  while(true){
    print("${dataBatasSuhu[satuanAwal][2]}, ${dataBatasSuhu[satuanAkhir][2]}, ${dataBatasSuhu[satuanAwal][0]}, ${dataBatasSuhu[satuanAkhir][1]}");
    double suhuAkhir=((dataBatasSuhu[satuanAkhir][2]/dataBatasSuhu[satuanAwal][2])*(suhuAwal-dataBatasSuhu[satuanAwal][0])+dataBatasSuhu[satuanAkhir][0]);
    if (suhuAkhir==suhuAkhir.floor()){
      return suhuAkhir.floor();
    } else{
    return suhuAkhir;
    }
  }
}