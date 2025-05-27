from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Load model hanya sekali
model = load_model("model\inception_resnet_model (1).keras")

# Label klasifikasi sesuai urutan saat training
label_map = {
    0: "jalan berlubang",
    1: "jalan retak",
    2: "jalan tidak rusak"
}

def klasifikasikan_gambar(image: Image.Image) -> str:
    # Preprocessing sesuai input model (ubah sesuai kebutuhan model kamu)
    img = image.resize((224, 224))  # ganti ukuran sesuai model kamu
    img_array = np.array(img) / 255.0  # normalisasi
    img_array = img_array.reshape((1, 224, 224, 3))  # batch dimension

    # Prediksi
    predictions = model.predict(img_array)
    label_index = np.argmax(predictions)
    return label_map[label_index]
#.venv\Scripts\activate