from action import downloadAction
from testdata import page_data

def action():

    html = downloadAction.getHtml(page_data.picture_url)
    imglist = downloadAction.downloadImg(html, page_data.img_pattern)
    filePath = downloadAction.defineFilePath()
    page_data.count = downloadAction.saveImgLocal(imglist, filePath, page_data.count)


if __name__ == '__main__':

    action()