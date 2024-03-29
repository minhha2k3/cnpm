from app.models import BenhNhan, ChiTietBenhNhan, LichKham, DanhSachKhamBenh, Manager, Favor, CMND, BHYT, Address, \
    UserRoleEnum, Config, LoaiThuoc, DonViThuoc, LoaiThuoc_DonViThuoc, DsLieuLuongThuoc, PhieuKhamBenh, HoaDonThanhToan
from app import app
import hashlib


def get_chitietbenhnhan_by_benhnhan_id(benhnhan_id):
    chitietbenhnhan = None

    if benhnhan_id:
        chitietbenhnhan = ChiTietBenhNhan.query.filter_by(benhnhan_id=benhnhan_id).first()

    return chitietbenhnhan


def get_chitietbenhnhan_by_sdt(sdt):
    chitietbenhnhan = None

    if sdt:
        chitietbenhnhan = ChiTietBenhNhan.query.filter_by(sdt=sdt).first()

    return chitietbenhnhan


def get_diachi_by_ctbn_id(ctbn_id):
    diachi = Address.query
    if ctbn_id:
        diachi = diachi.filter_by(chitiet_benhnhan_id=ctbn_id).first()

    return diachi


def get_diachi_by_ten_diachi(ten_diachi):
    diachi = Address.query
    if ten_diachi:
        diachi = diachi.filter_by(ten_diachi=ten_diachi).first()

    return diachi


def get_cmnd_by_ctbn_id(ctbn_id):
    cmnd = CMND.query
    if ctbn_id:
        cmnd = cmnd.filter_by(chitiet_benhnhan_id=ctbn_id).first()

    return cmnd


def get_bhyt_by_ctbn_id(ctbn_id):
    bhyt = BHYT.query
    if ctbn_id:
        bhyt = bhyt.filter_by(chitiet_benhnhan_id=ctbn_id).first()

    return bhyt


def get_value_by_key(key):
    value = Config.query
    if key:
        value = value.filter_by(key=key).first()

    return value


def get_cmnd_by_soCMND(soCMND):
    cmnd = CMND.query
    if soCMND:
        cmnd = cmnd.filter_by(so_cmnd=soCMND).first()

    return cmnd


def get_bhyt_by_soBHYT(soBHYT):
    bhyt = BHYT.query

    if soBHYT:
        bhyt = bhyt.filter_by(so_bhyt=soBHYT).first()

    return bhyt


def get_lichkham_by_ngaykham(ngaykham):
    lichkham = LichKham.query

    if ngaykham:
        lichkham = lichkham.filter_by(ngaykham=ngaykham).first()

    return lichkham


def get_danhsachkhambenh_theo_lichkham(ngaykham):
    lk = get_lichkham_by_ngaykham(ngaykham)
    return DanhSachKhamBenh.query.filter_by(lichkham_id=lk.id).all()


def get_danhsachkhambenh_by_lichkham_and_benhnhan(lichkham, benhnhan):
    return DanhSachKhamBenh.query.filter_by(lichkham_id=lichkham.id, benhnhan_id=benhnhan.id).all()


def count_danhsachkhambenh_theo_lichkham(id_lichkham):
    return DanhSachKhamBenh.query.filter_by(lichkham_id=id_lichkham).count()


def get_lichkham_by_id(id_lichkham):
    return LichKham.query.get(id_lichkham)


def get_duplicate_dangkikhambenh_by_2id(id_bn, id_lk):
    dangkikhambenh = DanhSachKhamBenh.query.filter_by(benhnhan_id=id_bn, lichkham_id=id_lk).first()

    return dangkikhambenh


def load_loaithuoc():
    return LoaiThuoc.query.all()


def load_donvithuoc():
    return DonViThuoc.query.all()


def get_loaithuoc_by_id(id):
    return LoaiThuoc.query.get(id)


def get_loaithuoc_by_tenloaithuoc(ten_loaithuoc):
    loaithuoc = LoaiThuoc.query

    if ten_loaithuoc:
        loaithuoc = loaithuoc.filter_by(ten_loaithuoc=ten_loaithuoc).first()

    return loaithuoc


def get_donvithuoc_by_id(id):
    return DonViThuoc.query.get(id)


def get_donvithuoc_by_tendonvithuoc(ten_donvithuoc):
    donvithuoc = DonViThuoc.query

    if ten_donvithuoc:
        donvithuoc = donvithuoc.filter_by(ten_donvithuoc=ten_donvithuoc).first()

    return donvithuoc


def get_loaithuoc_donvithuoc_by_id(id):
    return LoaiThuoc_DonViThuoc.query.get(id)


def get_loaithuoc_donvithuoc_by_2id(loaithuoc, donvithuoc):
    loaithuoc_donvithuoc = LoaiThuoc_DonViThuoc.query.filter_by(donvithuoc_id=donvithuoc.id,
                                                                loaithuoc_id=loaithuoc.id).first()
    return loaithuoc_donvithuoc


def get_loaithuoc_donvithuoc_by_2id2(id1, id2):
    loaithuoc_donvithuoc = LoaiThuoc_DonViThuoc.query.filter_by(donvithuoc_id=id1,
                                                                loaithuoc_id=id2).first()
    return loaithuoc_donvithuoc


def get_phieukhambenh_by_id(id):
    return PhieuKhamBenh.query.get(id)


def get_dsLieuLuongThuoc_by_phieuKhamBenh_id(id):
    dsll = DsLieuLuongThuoc.query
    if id:
        dsll = dsll.filter_by(phieukhambenh_id=id).all()

    return dsll


def get_hoadonthanhtoan_by_id(id):
    return HoaDonThanhToan.query.get(id)


# Authenticate Manager :

def get_manager_by_id(id):
    return Manager.query.get(id)


def get_benhnhan_by_id(id):
    return BenhNhan.query.get(id)


def auth_manager(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return Manager.query.filter(Manager.username.__eq__(username.strip()),
                                Manager.password.__eq__(password)).first()
