import cv2
import pytesseract
from PIL import Image
from tkinter import Tk, filedialog

# Jika Anda menggunakan Windows, Anda perlu mengatur path ke tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_from_image(image_path):
    img = Image.open(image_path)
    
    img = img.convert('L')
    
    # Baca gambar dengan OpenCV
    img = cv2.imread(image_path)
    
    # Konversi ke grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Thresholding biner
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Simpan gambar hasil thresholding
    cv2.imwrite('thresholded_image.png', thresh)
    
    # Gunakan Pillow untuk membuka gambar hasil thresholding
    img_pil = Image.fromarray(thresh)
    text = pytesseract.image_to_string(img_pil, lang='eng')
    return text

def capture_from_camera():
    # Buka kamera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Tidak dapat membuka kamera.")
        return
    
    while True:
        # Ambil frame dari kamera
        ret, frame = cap.read()
        
        # Tampilkan frame
        cv2.imshow('Kamera - Tekan SPACE untuk ambil gambar, ESC untuk keluar', frame)
        
        # Tunggu tombol keyboard
        key = cv2.waitKey(1)
        
        # Jika tombol SPACE ditekan, ambil gambar
        if key == 32:  # 32 adalah kode untuk SPACE
            image_path = 'captured_image.png'
            cv2.imwrite(image_path, frame)
            print(f"Gambar disimpan sebagai {image_path}")
            break
        
        # Jika tombol ESC ditekan, keluar
        if key == 27:  # 27 adalah kode untuk ESC
            print("Keluar tanpa mengambil gambar.")
            cap.release()
            cv2.destroyAllWindows()
            return
    
    # Lepaskan kamera dan tutup jendela
    cap.release()
    cv2.destroyAllWindows()
    
    return image_path

def select_from_file_manager():
    # Buka file manager untuk memilih gambar
    root = Tk()
    root.withdraw()  # Sembunyikan jendela utama
    file_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    
    return file_path

def main():
    print("Pilih sumber gambar:")
    print("1. Ambil gambar dari kamera")
    print("2. Pilih gambar dari file manager")
    choice = input("Masukkan pilihan (1/2): ")
    
    if choice == '1':
        image_path = capture_from_camera()
    elif choice == '2':
        image_path = select_from_file_manager()
    else:
        print("Pilihan tidak valid.")
        return
    
    if image_path:
        print("Melakukan OCR...")
        text = ocr_from_image(image_path)
        print("Hasil OCR:")
        print(text)
    else:
        print("Tidak ada gambar yang dipilih.")

if __name__ == "__main__":
    main()