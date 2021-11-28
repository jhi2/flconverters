#!/usr/bin/env python3

from converters import txtconvert, imgconvert, sheetconvert
import os

class test():
    def __init__(self, inputp, outp):
        self.inputp = inputp
        self.outp = outp

    def txtconverter(self):
        txtcsvoutpath = os.path.join(self.outp, 'txt_docx')
        convtxtdocx = txtconvert(__file__ = self.inputp, __d__ = txtcsvoutpath)
        print('* Running txt to csv')
        convtxtdocx.txt_docx()
        print('\nimg to pdf done!\n')

    def images(self):
        pdfimgoutpath = os.path.join(self.outp, 'img_pdf')
        convimgpdf = imgconvert(__file__ = self.inputp, __d__ = pdfimgoutpath)
        print('* Running img to pdf')
        convimgpdf.img_pdf()
        print('\nimg to pdf done!\n')

        img64outpath = os.path.join(self.outp, 'img64')
        convimg64 = imgconvert(__file__ = self.inputp, __d__ = img64outpath)
        print('* Running img to base64')
        convimg64.img_base64()
        print('\nimg to base64 done!\n')

        imgbinaryoutpath = os.path.join(self.outp, 'img_binary')
        convimgbinary = imgconvert(__file__ = self.inputp, __d__ = imgbinaryoutpath)
        print('* Running img to binary')
        convimgbinary.img_base64()
        print('\nimg to binary done!\n')

        imgjpegoutpath = os.path.join(self.outp, 'img_format')
        convimgjpeg = imgconvert(__file__ = self.inputp, __d__ = imgjpegoutpath)
        print('* Running img to jpeg')
        convimgjpeg.img_format(format = '.jpeg')
        print('\nimg to jpeg done!\n')

    def spread(self):
        outpath = os.path.join(self.outp, 'sheet_outputs')
        conv = sheetconvert(__file__ = self.inputp, __d__ = outpath)
        print('* Running xlsx to csv')
        conv.convertsh(fromtype = '.xlsx', totype = '.csv')
        print('\nxlsx to csv done!\n')


if __name__ == "__main__":
    cwd = os.getcwd()
    testsp = os.path.join(cwd, 'tests')
    testfls = os.path.join(testsp,'test_files')
    outs = os.path.join(cwd, 'Output')
    x = test(inputp = testfls, outp = outs)
    x.txtconverter()
    x.images()
    x.spread()

