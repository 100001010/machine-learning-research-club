#需要安裝tensorflow模組
#使用pip install tensorflow來安裝

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tensorflow.keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# 訓練用的圖片及標籤6萬筆, 測試用的圖片及標籤1萬筆

# 畫出手寫數字圖片train_images，共六萬筆；另有test_images，共一萬筆
import matplotlib.pyplot as plt

plt.gcf().set_size_inches(15, 4)                        #←設定圖形的寬和高 (英吋)
for i in range(10):                             #先顯示前10筆內容
    ax = plt.subplot(1, 10, 1+i)                    #←設定 1x10 的子圖表, 目前要畫第 1+i 個
    ax.imshow(train_images[i], cmap= 'gray')               #←顯示灰階圖片(黑底白字)，每個點為0~255的數值
    ax.set_title('label = '+str(train_labels[i]), fontsize=18)      #←設定標題
plt.show()   

# 預處理mnist輸入資料，有兩類，train和test，都要把灰度轉換成0~1之間的數值
x_train = train_images.reshape((60000, 28 * 28))              #←將 (60000,28,28) 轉換成 (60000,784)，即把照片改為一維度，共六萬筆資料
x_train = x_train.astype('float32') / 255                  #←再將 0~255 的像素值強迫轉換成 0~1 的浮點數(因為Keras預設適合輸入靠近0的數值)

x_test = test_images.reshape((10000, 28 * 28))               #←將 10000 筆測試樣本做同樣的轉換
x_test = x_test.astype('float32') / 255                   

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 預處理圖片資料，把資料改為一維度的。
# 預處理標籤資料，把答案改為One-hot編碼
# 預處理標籤資料(答案)
from tensorflow.keras.utils import to_categorical

y_train = to_categorical(train_labels)                    #←將訓練標籤做 One-hot 編碼(例：5轉為[0,0,0,0,0,1,0,0,0,0])
y_test  = to_categorical(test_labels)                    #←將測試標籤做 One-hot 編碼

print("預處理前標籤train_labels[0]={}, 預處理後標籤y_train[0]={}".format(train_labels[0],y_train[0]))
print("預處理前的訓練資料形狀屬性train_labels.shape={}, 預處理前的測試資料形狀屬性test_labels.shape={}".format(train_labels.shape,test_labels.shape)) #顯示為六萬及一萬筆陣列(不是數字)
print("預處理後的訓練資料形狀屬性x_train.shape={}, 預處理後的測試資料形狀屬性x_test.shape={}".format(x_train.shape,x_test.shape)) #顯示(輸入資料屬性，每筆為784個變量的向量)
print("預處理後的訓練標籤形狀屬性y_train.shape={}, 預處理後的測試標籤形狀屬性y_test.shape={}".format(y_train.shape,y_test.shape)) #顯示(標籤資料屬性，每筆為10個變量的向量)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 建立神經模型，基礎神經網路模型為序列式Sequential，第一層512個神經元，第二層10個(輸出層)
# 顯示神經模型摘要資訊
# 編譯神經模型 優化器介紹
# 建立多元分類模型
from tensorflow.keras.models import Sequential                #← 匯入 Keras 的序列式模型類別
from tensorflow.keras.layers import Dense                  #← 匯入 Keras 的密集層類別

print("建立神經模型...")
model = Sequential()                             #← 建立序列模型物件
model.add(Dense(512, activation='relu', input_dim= 784))           #← 加入第一層(密集層神經元512個，輸出層啟動函數為relu:負數全部當作0,輸入層為784個特徵數)
model.add(Dense(10, activation='softmax'))                   #← 加入第二層(密集層神經元10個，輸出層啟動函數為softmax輸出範圍介於0~1)，這就是輸出層了。p.s.啟動函數為tanh:輸出範圍介於-1~1

print("顯示模型的摘要資訊：")
model.summary()                                 #顯示模型的摘要資訊

model.compile(optimizer='rmsprop',                       #← 指定優化器
       loss='categorical_crossentropy',                 #← 指定損失函數(categorical_crossentropy：交叉分類熵)
       metrics=['acc'])                         #← 指定評量準則accuracy可簡寫為acc

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 訓練模型：將所有資料重複使用，共五週期訓練，每次128筆，每週期為60000/128約等469次
# 評估訓練成效
# 訓練模型
print("訓練開始：")
history = model.fit(x_train, y_train, epochs=10, batch_size=128)      #model.fit(訓練資料, 訓練答案, 訓練週期epochs, 每週期訓練筆數)，60000/128約等於469次

test_loss, test_acc = model.evaluate(x_test, y_test)            #←使用測試樣本及標籤來評估普適能力，每次32筆
print('計算對整個測試資料集的損失率：', test_loss)
print('計算對整個測試資料集的準確率：', test_acc)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 用樣本測試
# 畫出測試圖片並標示預測結果與標準答案
print("畫出測試圖片並標示預測結果與標準答案")
predict = model.predict(x_test)                    #←儲存所有測驗用樣本的預測結果(測試樣本全部代入預測模型)
import numpy as np
predict = np.argmax(predict,axis=1)

plt.gcf().set_size_inches(15, 4)                        #←設定圖形尺吋的寬和高(英吋)
for i in range(10):                             #列印出前10筆的結果
    ax = plt.subplot(1, 10, 1+i)                     #←設定 1x10 的子圖表, 目前要畫第 1+i 個
    ax.imshow(test_images[i], cmap='binary')                #←顯示圖片(白底黑字)
    ax.set_title('label = '+str(test_labels[i]) +            #設定顯示標準答案
           '\npredi = '+str(predict[i]), fontsize=18)       #←設定預測的答案
    ax.set_xticks([]); ax.set_yticks([])                  #←X, Y 軸不顯示刻度
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 儲存模型
model.save("C:\\Users\\josha\\Desktop\\python\\nmist\\Model.h5") #save model