import os
import uuid
from ffmpy import FFmpeg


# 图片裁剪
def cut_out_pic(image_path: str, output_dir: str, start_pix: tuple, size: tuple):
    ext = os.path.basename(image_path).strip().split('.')[-1]
    if ext not in ['png', 'jpg']:
        raise Exception('format error')
    result = os.path.join(output_dir, '{}.{}'.format(uuid.uuid1().hex, ext))
    ff = FFmpeg(inputs={image_path: None},
                outputs={result: '-vf crop={}:{}:{}:{} -y'.format(size[0], size[1], start_pix[0], start_pix[1])})
    print(ff.cmd)
    ff.run()
    return result


if __name__ == '__main__':
    #四个参数默认分别是图片地址，生成图片的保存地址、裁剪的起始像素坐标、裁剪的高和宽
    cut_out_pic(r'D:\系统默认\桌面\Work\numberAI\微信图片_20220713142728.jpg', r'D:\系统默认\桌面\Work', (145, 904), (100, 37))

