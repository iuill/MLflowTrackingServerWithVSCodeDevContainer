#
# h2oをダウンロードし、zip展開、元のzipファイルを削除する
#

$url = "https://h2o-release.s3.amazonaws.com/h2o/rel-3.42.0/2/h2o-3.42.0.2.zip"
$file = ".\h2o-3.42.0.2.zip"
$expand_dir = ".\dev_h2o\"

Invoke-WebRequest -Uri $url -OutFile $file
Expand-Archive -Path $file -DestinationPath $expand_dir
Remove-Item -Path $file
