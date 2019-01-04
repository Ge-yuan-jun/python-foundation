## week1

### type of knowledge

1. declarative knowledge: 陈述性知识
    - 事实陈述 (statements of facts)
2. imperative knowledge：程序性知识
    - 操作方法 ("how to" methods or recipes)

### basic machine architecture

1. memory (存储)
2. control unit (控制单元)：按照指令序列的顺序来执行
3. apithmetic logic unit (运算单元)

图灵完备：6种原语（primitives）可以计算任何东西

`The computer executes the instructions mostly in a linear sequence, except sometimes it jumps to a different place in the sequence.`
计算机大部分时候以线性顺序执行指令，除了有时它将跳转到序列的不同地方。

### programming language characteristics

关于语言：

1. primitive constructs (原语结构)
    - numbers, strings, simple operators
2. syntax (语法) - which strings of characters and symbols are well-formed
3. static semantic (静态语义) - which syntactically valid strings have a meaning (把东西放在一起形成合法表达式)
4. semantics (全语义) - what is the meaning associated with a syntactially correct string of symbols with no static semantic errors (按照语法把字符串和符号组合在一起，而且没有静态语义错误的句子)

program 易发生错误之处：

1. syntatic errors： common but easily caught by computer
2. static semantic errors
3. programs don't have semantics errors, but meaning may not be what was intended
    - crash
    - runs forever
    - produce a answer, but not expected