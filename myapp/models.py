from django.db import models
from django.core.validators import FileExtensionValidator
import os
# Create your models here.

#ファイルのアップロードを行うクラスを作成する。
#クラス内で宣言した変数すべてを総括して.objectsで呼び出すことができる。
class FileUpLoad(models.Model):
    title=models.CharField(max_length=50, default='')
    #CSVファイルのみアップロードできるようにする。
    upload_dir = models.FileField(upload_to='csv',validators=[FileExtensionValidator(['csv',])])
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def file_name(self):
        #相対パス(FileField)から名前のみ抽出する。
        path=os.path.basename(self.upload_dir.name)
        return path