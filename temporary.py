import numpy as np
import glob as glob
import matplotlib.pyplot as plt
import cv2
import os
import nibabel as nib
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
from tensorflow.keras.utils import to_categorical


class BRATS_Preprocess:


    def _init_(self):
        pass



    def zero_padding_function(self,mri_img):

        dim_1=int((240 - mri_img.shape[0]) / 2)
        dim_2=int((240 - mri_img.shape[1]) / 2)
        dim_3=int((144 - mri_img.shape[2]) / 2)

        # dim_3=0

        new_image=np.pad(mri_img, ((dim_1, dim_1), (dim_2, dim_2), (dim_3, dim_3)), constant_values=0)

        if new_image.shape[2] < 144:
            new_image=np.pad(new_image, ((0, 0), (0, 0), (1, 0)), constant_values=0)

            pass

        return new_image
        pass

    def resize_function(self, img_slice):

        new_reshape_slice = cv2.resize(np.array(img_slice).astype(np.uint8), (240, 240,144))


        return new_reshape_slice
        pass

    def read_data(self, data_path, save_path):

        reshape_or_zero_padding_flag = 0

        cbf_files, cbv_files, dwi_files, t1c_files, t2_files, tmax_files, ttp_files=[], [], [], [], [], [], []
        gt_files=[]
        files=glob.glob(data_path + '\\**\\**\\*.nii')
        print(files)
        print("#" * 40)

        for file in files:
            if 'CBF' in file:
                cbf_files.append(file)
            elif 'CBV' in file:
                cbv_files.append(file)
            elif 'DWI' in file:
                dwi_files.append(file)
            elif 'T1c' in file:
                t1c_files.append(file)
            elif 'T2' in file:
                t2_files.append(file)
            elif 'Tmax' in file:
                tmax_files.append(file)
            elif 'TTP' in file:
                ttp_files.append(file)
            elif 'OT' in file:
                gt_files.append(file)

        print(len(cbf_files), len(cbv_files), len(dwi_files), len(t1c_files), len(t2_files), len(tmax_files),
              len(ttp_files), len(gt_files))

        all_files = zip(cbf_files, cbv_files, dwi_files, t1c_files, t2_files, tmax_files, ttp_files, gt_files)
        cbf_img=cbv_img=dwi_img=t1c_img=t2_img=tmax_img=ttp_img=gt_img=[]
        j=0

        for cbf, cbv, dwi, t1c, t2, tmax, ttp, gt in all_files:

            j = j + 1

            print("Now preparing image : ", j)

            cbf_img=nib.load(cbf).get_fdata()
            cbv_img=nib.load(cbv).get_fdata()
            dwi_img=nib.load(dwi).get_fdata()
            t1c_img=nib.load(t1c).get_fdata()
            t2_img=nib.load(t2).get_fdata()
            tmax_img=nib.load(tmax).get_fdata()
            ttp_img=nib.load(ttp).get_fdata()
            gt_img=nib.load(gt).get_fdata()



            cbf_img = self.zero_padding_function(cbf_img)

            dwi_img = self.zero_padding_function(dwi_img)

            tmax_img = self.zero_padding_function(tmax_img)
            ttp_img = self.zero_padding_function(ttp_img)

            gt_img = self.zero_padding_function(gt_img)


            cbf_img = scaler.fit_transform(cbf_img.reshape(-1, cbf_img.shape[-1])).reshape(
                cbf_img.shape)

            dwi_img = scaler.fit_transform(dwi_img.reshape(-1, dwi_img.shape[-1])).reshape(
                dwi_img.shape)

            tmax_img = scaler.fit_transform(tmax_img.reshape(-1, tmax_img.shape[-1])).reshape(
                tmax_img.shape)

            ttp_img = scaler.fit_transform(ttp_img.reshape(-1, ttp_img.shape[-1])).reshape(
                ttp_img.shape)


            gt_img = gt_img.astype(np.uint8)

            labels = np.unique(gt_img)

            #labels updation

            gt_img[gt_img == 1] = 6
            gt_img[gt_img == 2] = 5


            #print()
            #print(np.unique(gt_img))


            temp_combined_images=np.stack([cbf_img, dwi_img, tmax_img, ttp_img], axis=3)

            gt_img = to_categorical(gt_img, num_classes=7)

            #print(temp_combined_images.shape)
            #print()
            #print(gt_img.shape)

            np.savez_compressed('E:/Nosheen/BRATS2017/npz files/SPES_2015_npz/image_' + str(j), a=temp_combined_images,b=gt_img)


            """ print(np.unique(cbf_img))
            print(np.unique(dwi_img))
            print(np.unique(tmax_img))
            print(np.unique(ttp_img))"""



            print("Saved !")

            pass



        pass


    pass

path = "E:/Nosheen/ISLES2015/SPES2015_Training"

isles_npz_class = BRATS_Preprocess()

isles_npz_class.read_data(data_path=path,save_path="")
