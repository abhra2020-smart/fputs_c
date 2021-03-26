from distutils.core import setup, Extension


def main():
    setup(name="fputs",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="Abhradeep De",
          author_email="deabhradeep@gmail.com",
          ext_modules=[Extension("fputs", ["fputs.c"], language='c')])


if __name__ == "__main__":
    main()
