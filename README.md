# ML_Pipelinee
Pipeline adalah cara sederhana untuk menjaga prapemrosesan data dan kode pemodelan Anda tetap teratur. Secara khusus, pipeline menggabungkan 
langkah-langkah prapemrosesan dan pemodelan sehingga Anda dapat menggunakan seluruh bundel seolah-olah itu adalah satu langkah.
-cleaner code:
Akuntansi data pada setiap langkah prapemrosesan bisa menjadi berantakan. 
Dengan pipeline, Anda tidak perlu melacak data pelatihan dan validasi secara manual di setiap langkah.

-fewer bug:
peluang untuk salah dalam penerapan langkah di setiap pemprosesan lebih sedikit

-Easier to Productionize:
kesulitan dalam mentrasisikan dari prototype ke dalam sebuah penerapan skala besar dengan pipeline masalah
tersebut dapat di selesaikan dengan mudah

-More options for data validation
ada banyak jenis option untuk memvalidasi data contohnya adalah teknik
cover cross-validasi
=>Dengan pipeline, kami melakukan praproses data pelatihan dan menyesuaikan model dalam satu baris kode. 
(Sebaliknya, tanpa pipeline, kita harus melakukan imputasi, one-hot encoding, 
dan pelatihan model dalam langkah-langkah terpisah. Ini menjadi sangat berantakan jika kita harus berurusan dengan variabel numerik dan kategoris!)    

=Dengan pipeline, kami menyediakan fitur yang belum diproses di X_valid ke perintah predict(), dan pipeline secara otomatis memproses fitur 
sebelum menghasilkan prediksi. (Namun, tanpa pipeline, kita harus ingat untuk melakukan praproses data validasi sebelum membuat prediksi.)
Pipeline berguna untuk membersihkan kode pembelajaran mesin dan menghindari kesalahan, dan sangat berguna untuk alur kerja dengan prapemrosesan data yang canggih.
