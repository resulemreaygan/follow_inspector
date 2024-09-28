# FollowInspector - Takipçi Karşılaştırma Aracı

## English

### Overview

FollowInspector is a Python script that allows you to compare your Instagram followers and followings from the data you
download. It helps you find out who you follow but who doesn't follow you back, and who follows you but you don't follow
back. This simple tool can be used anytime.

### Features

- Compares followings and followers.
- Lists the people you follow who don't follow you back with their profile links.
- Lists the people who follow you but you don't follow back with their profile links.
- Easy to use and lightweight.

### Requirements

- Python 3.11
- PyYAML

### Installation and Setup

Follow the steps below to set up the project environment using Miniconda:

1. **Download and Install Miniconda**: If you don't have Miniconda or Anaconda installed, download and install Miniconda
   from [here](https://docs.conda.io/en/latest/miniconda.html).

2. **Create a New Environment**:
   ```bash
   conda create --name followinspector python=3.11
   ```
   This command will create a new environment named `followinspector` with Python 3.11.

3. **Activate the Environment**:
   ```bash
   conda activate followinspector
   ```

4. **Install the Required Packages**:
   ```bash
   pip install pyyaml
   ```

5. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourremreaygan/FollowInspector.git
   cd FollowInspector
   ```

6. **Create a `config.yaml` file in the project directory** with the following content:
   ```yaml
   followers_file: "/path/to/followers.json"
   followings_file: "/path/to/followings.json"
   ```
   Replace `/path/to/followers.json` and `/path/to/followings.json` with the actual paths of your Instagram data files.

### Running the Script

1. **Edit the Configuration**: Make sure the `config.yaml` file has the correct paths for the followers and followings
   JSON files.

2. **Run the Script**:
   ```bash
   python follow_inspector.py
   ```

3. **Script Output**:
    - It will show two lists:
        1. People who don't follow you back, along with their profile links.
        2. People who follow you but you don't follow back, along with their profile links.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Türkçe

### Genel Bakış

FollowInspector, Instagram'dan indirdiğiniz verilerle takip ettiklerinizi ve takipçilerinizi karşılaştırmanıza olanak
tanıyan bir Python scriptidir. Bu araç sayesinde, sizin takip ettiğiniz ancak sizi takip etmeyen kişileri ve sizi takip
eden ama sizin geri takip etmediğiniz kişileri kolayca bulabilirsiniz. Basit ve her zaman kullanılabilecek bir araçtır.

### Özellikler

- Takip edilenleri ve takipçileri karşılaştırır.
- Sizi geri takip etmeyen kişileri ve profillerini listeler.
- Sizi takip eden ama sizin geri takip etmediğiniz kişileri ve profillerini listeler.
- Kullanımı kolay ve hafif bir araçtır.

### Gereksinimler

- Python 3.11
- PyYAML

### Kurulum ve Ayarlar

Projeyi Miniconda kullanarak kurmak için aşağıdaki adımları izleyin:

1. **Miniconda'yı İndirin ve Kurun**: Eğer Miniconda veya Anaconda yüklü
   değilse, [buradan](https://docs.conda.io/en/latest/miniconda.html) Miniconda'yı indirin ve kurun.

2. **Yeni Bir Ortam Oluşturun**:
   ```bash
   conda create --name followinspector python=3.11
   ```
   Bu komut, `followinspector` adında Python 3.11 içeren bir ortam oluşturacaktır.

3. **Ortamı Aktif Edin**:
   ```bash
   conda activate followinspector
   ```

4. **Gerekli Paketleri Yükleyin**:
   ```bash
   pip install pyyaml
   ```

5. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/yourremreaygan/FollowInspector.git
   cd FollowInspector
   ```

6. **Proje dizininde `config.yaml` dosyası oluşturun** ve aşağıdaki içeriği ekleyin:
   ```yaml
   followers_file: "/path/to/followers.json"
   followings_file: "/path/to/followings.json"
   ```
   `/path/to/followers.json` ve `/path/to/followings.json` yollarını kendi Instagram veri dosyalarınızın konumu ile
   değiştirin.

### Scripti Çalıştırma

1. **Konfigürasyonu Düzenleyin**: `config.yaml` dosyasındaki takipçi ve takip edilen JSON dosyalarının yolunun doğru
   olduğundan emin olun.

2. **Scripti Çalıştırın**:
   ```bash
   python follow_inspector.py
   ```

3. **Script Çıktısı**:
    - İki liste görüntülenecektir:
        1. Sizi geri takip etmeyen kişilerin listesi ve profil bağlantıları.
        2. Sizi takip eden ama sizin geri takip etmediğiniz kişilerin listesi ve profil bağlantıları.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
