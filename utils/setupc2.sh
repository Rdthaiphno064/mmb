#!/bin/bash

# Kiểm tra quyền root
if [ "$EUID" -ne 0 ]; then
  echo "Vui lòng chạy script này với quyền root (sudo)"
  exit 1
fi

# Hàm cài đặt hệ thống
install_system() {
  echo "Cập nhật hệ thống và cài đặt công cụ..."
  apt update -y
  apt install -y python3 ufw net-tools wget curl

  # Tăng giới hạn file descriptor
  echo "Tăng giới hạn file descriptor..."
  echo "* soft nofile 10000" >> /etc/security/limits.conf
  echo "* hard nofile 10000" >> /etc/security/limits.conf
  echo "fs.file-max = 2097152" >> /etc/sysctl.conf

  # Tối ưu mạng
  echo "Tối ưu hóa mạng..."
  cat <<EOL >> /etc/sysctl.conf
net.core.somaxconn = 65535
net.ipv4.ip_local_port_range = 1024 65535
net.ipv4.tcp_tw_reuse = 1
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
EOL
  sysctl -p

  # Cấu hình UFW
  echo "Cấu hình UFW để mở port 2323 và 1002..."
  ufw allow in to any port 2323 proto tcp
  ufw allow out to any port 2323 proto tcp
  ufw allow in to any port 1002 proto tcp
  ufw allow out to any port 1002 proto tcp
  ufw --force enable

  # Tải file se.py
  echo "Tải file se.py từ GitHub..."
  wget -O se.py https://github.com/Rdthaiphno064/mmb/raw/refs/heads/main/utils/se.py
  if [ $? -eq 0 ]; then
    echo "Tải se.py thành công!"
    chmod +x se.py
  else
    echo "Lỗi khi tải se.py, thử dùng curl..."
    curl -o se.py https://github.com/Rdthaiphno064/mmb/raw/refs/heads/main/utils/se.py
    if [ $? -eq 0 ]; then
      echo "Tải se.py thành công bằng curl!"
      chmod +x se.py
    else
      echo "Không thể tải se.py. Vui lòng kiểm tra kết nối mạng hoặc URL."
      exit 1
    fi
  fi
}

# Hàm tạo systemd service để đảm bảo se.py luôn chạy và tự khởi động
setup_service() {
  echo "Tạo systemd service cho se.py..."
  cat <<EOL > /etc/systemd/system/se-py.service
[Unit]
Description=se.py Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /root/se.py
WorkingDirectory=/root
Restart=always
RestartSec=5
User=root
StandardOutput=append:/root/se.log
StandardError=append:/root/se.log

[Install]
WantedBy=multi-user.target
EOL

  # Di chuyển se.py đến /root nếu chưa ở đó
  if [ ! -f /root/se.py ]; then
    mv se.py /root/
  fi

  # Reload systemd và kích hoạt service
  systemctl daemon-reload
  systemctl enable se-py.service
  systemctl start se-py.service

  echo "Service se-py đã được tạo và khởi động!"
}

# Hàm kiểm tra và chạy se.py
check_and_run() {
  if systemctl is-active se-py.service > /dev/null 2>&1; then
    echo "se.py đang chạy. Trạng thái:"
    systemctl status se-py.service --no-pager
  else
    echo "se.py không chạy, khởi động lại..."
    systemctl start se-py.service
  fi
}

# Logic chính
if [ ! -f /root/se.py ]; then
  echo "se.py chưa tồn tại, tiến hành cài đặt..."
  install_system
  setup_service
else
  echo "se.py đã tồn tại, kiểm tra và chạy..."
  if [ ! -f /etc/systemd/system/se-py.service ]; then
    setup_service
  fi
  check_and_run
fi

# Kiểm tra trạng thái cuối cùng
echo "Kiểm tra cấu hình..."
ufw status
ss -tuln | grep -E "2323|1002"
ulimit -n
echo "Trạng thái se.py:"
systemctl status se-py.service --no-pager

echo "Hoàn tất!"