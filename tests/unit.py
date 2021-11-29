#!/usr/bin/env python3

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from converters import txtconvert, imgconvert, sheetconvert

class test():
    """Wrapper function for unit testing the converters library.
    """

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
