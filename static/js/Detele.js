function confirmDelete(button) {
    // เรียกใช้ SweetAlert
    Swal.fire({
        title: 'คุณแน่ใจหรือไม่?',
        text: "ข้อมูลที่ถูกลบจะไม่สามารถกู้คืนได้!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'ยืนยันการลบ',
        cancelButtonText: 'ยกเลิก'
    }).then((result) => {
        if (result.isConfirmed) {
            // ถ้าผู้ใช้ยืนยัน ก็ให้ส่งฟอร์มไปเพื่อทำการลบ
            button.closest('form').submit();
        }
    })
}
