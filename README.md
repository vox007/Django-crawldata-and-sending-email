A) Cài đặt môi trường chạy project
1. Pull code từ github
2. Cài đặt python từ trang chủ : https://www.python.org/
3. Cài đặt pip ( trình quản lý gói ) cho python : pip install pip
4. Cài đặt các module của project:
- Vào thư mục chứa project và có file requirements.txt
- Cài đặt các module của project bằng cách sử dụng : pip install -r requirements.txt
5. Chờ hoàn tất các bước cài đặt

B) Cài đặt broker cho celery ( là một open source asynchronous task queue or job queue ) dùng để chạy các task của project:
1. Cài đặt redis (broker) : https://github.com/microsoftarchive/redis/releases
2. Thử chạy redis trong terminal bằng : redis-cli PING (nếu terminal phản hồi là PONG thì redis đã được cài đặt thành công)

C) Chạy môi trường project
1. Chạy live-server của Django bằng : python manage.py runserver
2. Chạy producer của celery (djang-celery-beat) : celery -A crawlweb beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
3. Chạy consumer của celery (worker) : celery -A crawlweb worker -l info


Cấu trúc thư mục của project:

1. manage.py: một CLI giúp ta tương tác nhanh với code Django
  crawlweb/__init__.py: Để chỉ cho python rằng thư mục này là một package.
  crawlweb/settings.py: Chứa các cấu hình của project
  crawlweb/urls.py: Định nghĩa các URL của project.
  crawlweb/wsgi.py: Dùng để deploy project của ta lên Server.

2. Thư mục crawldata:
  crawldata/admin.py: File giúp ta tạo các có thể thay đổi được trong trang quản trị
  crawldata/models.py: File chứa mã code của model , tạo ra các trường của bảng
  crawldata/tests.py: File chứa mã code của unit tests
  crawldata/views.py: file chứa các code của api
  crawldata/forms.py : nơi chứa các forms của project
  crawldata/tasks.py : nơi chứa các tasks của project (crawl data và gửi mail)
