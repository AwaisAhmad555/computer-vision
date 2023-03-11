import numpy as np
import glob as glob
import matplotlib.pyplot as plt
import cv2
import os
import nibabel as nib



class BRATS_Preprocess:


    def _init_(self):
        pass



    def zero_padding_function(self,img_slice):

        dim_1 = int((240 - img_slice.shape[0]) / 2)
        dim_2 = int((240 - img_slice.shape[1]) / 2)

        new_slice = np.pad(img_slice, ((dim_1, dim_1), (dim_2, dim_2)))


        return new_slice
        pass

    def resize_function(self, img_slice):

        new_reshape_slice = cv2.resize(np.array(img_slice).astype(np.uint8), (240, 240))


        return new_reshape_slice
        pass

    def read_data(self, data_path, save_path):

        reshape_or_zero_padding_flag = 0

        cbf_files, cbv_files, dwi_files, t1c_files, t2_files, tmax_files, ttp_files = [], [], [], [], [], [], []
        gt_files = []
        files = glob.glob(data_path + '\\**\\**\\*.nii')
        print(files)
        print("#" * 40)

        for file in files:
            if 'CBF' in file:
                cbf_files.append(file)
            elif 'CBV.' in file:
                cbv_files.append(file)
            elif 'DWI.' in file:
                dwi_files.append(file)
            elif 'T1c.' in file:
                t1c_files.append(file)
            elif 'T2.' in file:
                t2_files.append(file)
            elif 'Tmax.' in file:
                tmax_files.append(file)
            elif 'TTP.' in file:
                ttp_files.append(file)
            elif 'OT' in file:
                gt_files.append(file)

        print(len(cbf_files), len(cbv_files), len(dwi_files), len(t1c_files), len(t2_files), len(tmax_files),
              len(ttp_files), len(gt_files))



        all_files = zip(cbf_files, cbv_files, dwi_files, t1c_files, t2_files, tmax_files, ttp_files, gt_files)
        cbf_img = cbv_img = dwi_img = t1c_img = t2_img = tmax_img = ttp_img = gt_img = []
        j = 0


        for cbf, cbv, dwi, t1c, t2, tmax, ttp, gt in all_files:


            j = j + 1
            cbf_img = nib.load(cbf).get_fdata()
            cbv_img = nib.load(cbv).get_fdata()
            dwi_img = nib.load(dwi).get_fdata()
            t1c_img = nib.load(t1c).get_fdata()
            t2_img = nib.load(t2).get_fdata()
            tmax_img = nib.load(tmax).get_fdata()
            ttp_img = nib.load(ttp).get_fdata()
            gt_img = nib.load(gt).get_fdata()

            temp_combined_images = np.stack([cbf_img, cbv_img, dwi_img, t1c_img, t2_img, tmax_img, ttp_img], axis=3)


            #X = np.asarray([cbf_img, cbv_img, dwi_img, t1c_img, t2_img, tmax_img, ttp_img])


            Y = np.asarray(gt_img)




            pass



        pass



    pass


