from django.shortcuts import get_object_or_404, render
from .models import FileUpLoad
from django_pandas.io import pd
import io
import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse
import base64
import matplotlib
matplotlib.use('Agg')

# Create your views here.
#viewにて普通のプログラミングっぽいのが可能
def test2(req):
    file_obj=FileUpLoad.objects.all()
    context={
        'file_obj':file_obj,
    }
    return render(req,'test2.html',context)
    #reqが発生した際に、htmlにcontext(modelsで定義した)を受け渡す.

def detail(req,pk):
    file_value=get_object_or_404(FileUpLoad,id=pk)
    try:
        df=pd.read_csv(file_value.upload_dir.path,index_col=0,skip_blank_lines=True,skiprows=6)
    except UnicodeDecodeError:
        df=pd.read_csv(file_value.upload_dir.path,index_col=0,encoding='cp932',skip_blank_lines=True,skiprows=6)
    #df.drop(df.index[[1,2,3,4,5,6,7,8]])
    context={
            'file_value':file_value,
            'df':df,
    }
    return render(req,'detail.html',context)

def inputdata(pk):
    file_value=get_object_or_404(FileUpLoad,id=pk)
    try:
        df=pd.read_csv(file_value.upload_dir.path,skip_blank_lines=True,index_col=0,skiprows=6) 
    except UnicodeDecodeError:
        df=pd.read_csv(file_value.upload_dir.path,skip_blank_lines=True,index_col=0,encoding='cp932',skiprows=6)
    #df.drop(df.index[[1,2,3,4,5,6,7,8]])     #データフレームから余分な行を削除
    TestName="IREF"
    df.replace(' ','',regex=True,inplace=True)
    df.set_index('Test Item',inplace=True)
    Test = df.at[TestName,'data']
    n = len(Test)
    plt.hist(Test,bins=n,color="red")
    plt.xlabel("Current (uA)")
    plt.ylabel("Counts (-)")
    plt.xlim(Test.mean()-3*Test.std()*1.1,Test.mean()+3*Test.std()*1.1)
    plt.vlines(Test.mean()+3*Test.std(),0,max(Test),color="#5F9BFF",linestyle='dashed')
    plt.vlines(Test.mean()-3*Test.std(),0,max(Test),color="#5F9BFF",linestyle='dashed')

def conv():
    #ここのBytesIOで仮想メモリ確保している
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    #https://edge.sincar.jp/web/base64-inline-image/
    s=base64.b64encode(s).decode('utf-8')
    buf.close()
    return s

def histtests(req,pk):
    file_value=get_object_or_404(FileUpLoad,id=pk)
    inputdata(pk)            #plot図の作成
    response = conv()        #png形式に変換する。
    #response = HttpResponse(png, content_type='image/png')
    context={
            'file_value':file_value,
            'response':response,
    }
    plt.cla()        #いちおう初期化する。
    return render(req,'histtest.html',context)
    
     




#----------テスト用関数-------------------------------------------------------------
def inputdata_test(pk):
    file_value=get_object_or_404(FileUpLoad,id=pk)
    '''try:
        df=pd.read_csv(file_value.upload_dir.path,index_col=0) 
    except UnicodeDecodeError:
        df=pd.read_csv(file_value.upload_dir.path,index_col=0,encoding='cp932')
        '''
    #関数をプロットできるかのテスト
    fig=plt.figure()
    ax = fig.add_subplot(111)
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([20, 90, 50, 30, 100, 80, 10, 60, 40, 70])
    plt.plot(x, y)
#-----------------------------------------------------------------------------------