# 相机内参标定验证脚本

## 依赖
opencv
numpy
matplotlib

## 核心代码
```python
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1, (w,h))
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
```

## 使用
```python
python undistort_image_check.py
```
