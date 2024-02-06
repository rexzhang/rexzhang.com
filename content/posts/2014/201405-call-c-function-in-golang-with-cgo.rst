golang 使用 cgo 调用没有链接文件的动态链接库
########################################################


:author: Rex Zhang
:date: 2014-05-08T00:41:31+08:00
:modified: 2014-05-08T00:41:31+08:00
:status: published
:category: Coding
:tags: Go


获得符号表的方法

.. code-block:: shell

    nm libfoo.so

演示工程目录结构

.. code-block:: text

    ~/projectRoot
        bin
            libfoo.so
        script
            build.sh
        src
            libfoogo
                libforgo.go
            libfoogo_test
                main.go

构建脚本 ``build.sh``

.. code-block:: shell

    #!/bin/bash
    cd ../bin

    export GOPATH=~/projectRoot
    go build libfoogo_test

    cd ../script

使用cgo 接口做的库访问代码 ``libfoogo.go``

.. code-block:: golang

    package libfoogo

    //Go 语言中的 C 代码片段需要用 /* */ 注释框起来以便编译器知道
    /*
    #include <stdio .h>
    #include <stdlib .h>
    #include <dlfcn .h>
    #include <errno .h>

    #cgo LDFLAGS: -ldl //告知编译器链接 dlopen()要用到的库

    int (* funGet100k)(int i);

    void initDll() {
        void *handle;
        handle = dlopen("./libfoogo.so", RTLD_NOW);//RTLD_LAZY);//装载动态链接库
        if (!handle) {
            printf("!ERROR! dlopen error %d %s\n", errno, dlerror());//dlerror() 函数很有用，出现错误会有文字错误信息返回
            return;
            }
        funGet100k = dlsym(handle, "_ZN9RandomApi8Get_100kEj");//根据符号表信息获得动态链接库中函数的调用接口
        if (funGet100k == 0){
            printf("!ERROR! get null\n");
        }
        printf("init dll ok\n");
        return;
    }

    int Get100k(int i) {
        return funGet100k(i);
    }

    */
    import "C"

    //封装，供外部使用
    //这里要注意数据类型的转换
    func
    Get100k(n int) int
    {
        r: = C.Get100k(C.int(n)) return int(r)
    }

测试用工程的代码 ``main.go``

.. code-block:: golang

    package main

    import (
        "fmt"
        "libfoogo"
    )

    func main() {
        var data [101]int
        for i := 1; i < 1000; i++ {
            r := librandomgo.Get100k(100)//调用范例
            data[r] += 1
        }

        fmt.Println("------------------")
        for i := 0; i < 100; i++ {
            fmt.Println(i, ":", data[i])
        }
    }

另外官方推荐的还有一种渠道是用 SWIG

参考

cgo 相关资料

- http://golang.org/cmd/cgo/
- http://www.goinggo.net/2013/08/using-c-dynamic-libraries-in-go-programs.html
- https://code.google.com/p/go-wiki/wiki/cgo
- http://1.guotie.sinaapp.com/?p=435

dlopen() 相关资料

- http://tldp.org/HOWTO/Program-Library-HOWTO/dl-libraries.html
- http://linux.die.net/man/3/dlopen
- http://stackoverflow.com/questions/10765320/compile-c-program-using-dlopen-and-dlsym-with-fpic

Go 调用 SQLite 的（官方推荐）范例，没有使用 dlopen()
- https://code.google.com/p/gosqlite/source/browse/sqlite/sqlite.go
