class Database:
    def __enter__(self):
        print("اتصال به دیتابیس برقرار شد")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("اتصال به دیتابیس بسته شد")

with Database() as db:
    print("کار با دیتابیس")