import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
#TEST SHORT VARIABLE DECLARATION WITHOUT ARRAY TYPE
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = """Program([
\tVarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

        input = """x: float;"""
        expect = """Program([
\tVarDecl(x, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

        input = """a: string;"""
        expect = """Program([
\tVarDecl(a, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

        input = """aBc: boolean;"""
        expect = """Program([
\tVarDecl(aBc, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

        input = """_aBc_23: auto;"""
        expect = """Program([
\tVarDecl(_aBc_23, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

        input = """a, _aBc_23: auto;"""
        expect = """Program([
\tVarDecl(a, AutoType)
\tVarDecl(_aBc_23, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

        input = """a, x, b9x, _aBc_23: string;"""
        expect = """Program([
\tVarDecl(a, StringType)
\tVarDecl(x, StringType)
\tVarDecl(b9x, StringType)
\tVarDecl(_aBc_23, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

        input = """a, x, b9x, _aBc_23: string;
        c, _d2, e: float;"""
        expect = """Program([
\tVarDecl(a, StringType)
\tVarDecl(x, StringType)
\tVarDecl(b9x, StringType)
\tVarDecl(_aBc_23, StringType)
\tVarDecl(c, FloatType)
\tVarDecl(_d2, FloatType)
\tVarDecl(e, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

        input = """a, x, b9x, _aBc_23: string;
        c, _d2, e: float;
        mn: integer;"""
        expect = """Program([
\tVarDecl(a, StringType)
\tVarDecl(x, StringType)
\tVarDecl(b9x, StringType)
\tVarDecl(_aBc_23, StringType)
\tVarDecl(c, FloatType)
\tVarDecl(_d2, FloatType)
\tVarDecl(e, FloatType)
\tVarDecl(mn, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 308))






#TEST FUNCTION PROTOTYPE WITHOUT ARRAY TYPE
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

        input = """main: function void () inherit testFunc {
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], testFunc, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

        input = """main: function auto (x: boolean) {
        }"""
        expect = """Program([
\tFuncDecl(main, AutoType, [Param(x, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

        input = """main: function void (x: boolean, y: boolean) {
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(x, BooleanType), Param(y, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

        input = """main: function void (x: boolean, y: boolean, z: integer) {
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(x, BooleanType), Param(y, BooleanType), Param(z, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

        input = """main: function void (inherit x: boolean, out y: auto, inherit out z: integer) {
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [InheritParam(x, BooleanType), OutParam(y, AutoType), InheritOutParam(z, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

        input = """main: function void (inherit x: boolean, out y: auto, inherit out z: integer) inherit helloFunc {
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [InheritParam(x, BooleanType), OutParam(y, AutoType), InheritOutParam(z, IntegerType)], helloFunc, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))





# TEST SHORT VARIABLE DECLARATION WITH ARRAY TYPE
        input = """x: array[7, 8] of integer;"""
        expect = """Program([
\tVarDecl(x, ArrayType([7, 8], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

        input = """x: array[0] of integer;"""
        expect = """Program([
\tVarDecl(x, ArrayType([0], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

        input = """x: array[0,1,2] of boolean;"""
        expect = """Program([
\tVarDecl(x, ArrayType([0, 1, 2], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

        input = """a, x: string;
        x: array[0,1,2] of boolean;
        b, d: integer;"""
        expect = """Program([
\tVarDecl(a, StringType)
\tVarDecl(x, StringType)
\tVarDecl(x, ArrayType([0, 1, 2], BooleanType))
\tVarDecl(b, IntegerType)
\tVarDecl(d, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

        input = """a, x: string;
        x: array[0,1,2] of boolean;
        main: function void (x: boolean) {
        }
        b, d: integer;"""
        expect = """Program([
\tVarDecl(a, StringType)
\tVarDecl(x, StringType)
\tVarDecl(x, ArrayType([0, 1, 2], BooleanType))
\tFuncDecl(main, VoidType, [Param(x, BooleanType)], None, BlockStmt([]))
\tVarDecl(b, IntegerType)
\tVarDecl(d, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 320))




# TEST FUNCTION PROTOTYPE DECLARATION WITH ARRAY TYPE
        input = """helloFunc: function array[2] of integer() inherit welcomeFunc {}"""
        expect = """Program([
\tFuncDecl(helloFunc, ArrayType([2], IntegerType), [], welcomeFunc, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

        input = """helloFunc: function array[2,3] of string() {}"""
        expect = """Program([
\tFuncDecl(helloFunc, ArrayType([2, 3], StringType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

        input = """helloFunc: function array[2,3] of string(a: integer, out bb: auto) {}"""
        expect = """Program([
\tFuncDecl(helloFunc, ArrayType([2, 3], StringType), [Param(a, IntegerType), OutParam(bb, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))





# TEST EXPRESSION BY VARIABLE DECLARATION WHITHOUT FUNCALL
        input = """a: integer = 1;"""
        expect = """Program([
\tVarDecl(a, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

        input = """a: string = "Hello String \\b";"""
        expect = """Program([
\tVarDecl(a, StringType, StringLit(Hello String \\b))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

        input = """a: string = bcd;"""
        expect = """Program([
\tVarDecl(a, StringType, Id(bcd))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

        input = """a: string = 1 + 2;"""
        expect = """Program([
\tVarDecl(a, StringType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

        input = """a: string = 1 + 2 / 3 * 4;"""
        expect = """Program([
\tVarDecl(a, StringType, BinExpr(+, IntegerLit(1), BinExpr(*, BinExpr(/, IntegerLit(2), IntegerLit(3)), IntegerLit(4))))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

        input = """a: string = -1 + 2 / -3 * 4;"""
        expect = """Program([
\tVarDecl(a, StringType, BinExpr(+, UnExpr(-, IntegerLit(1)), BinExpr(*, BinExpr(/, IntegerLit(2), UnExpr(-, IntegerLit(3))), IntegerLit(4))))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

        input = """a: string = false && true || true :: "hello there";"""
        expect = """Program([
\tVarDecl(a, StringType, BinExpr(::, BinExpr(||, BinExpr(&&, BooleanLit(False), BooleanLit(True)), BooleanLit(True)), StringLit(hello there)))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

        input = """a: string = false == true;"""
        expect = """Program([
\tVarDecl(a, StringType, BinExpr(==, BooleanLit(False), BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

        input = """a: boolean = false && !true;"""
        expect = """Program([
\tVarDecl(a, BooleanType, BinExpr(&&, BooleanLit(False), UnExpr(!, BooleanLit(True))))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

        input = """a: integer = {1, 2, 3};"""
        expect = """Program([
\tVarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

        input = """a: integer = {-1.2, abc, "abc", true};"""
        expect = """Program([
\tVarDecl(a, IntegerType, ArrayLit([UnExpr(-, FloatLit(1.2)), Id(abc), StringLit(abc), BooleanLit(True)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

        input = """a: integer = {};"""
        expect = """Program([
\tVarDecl(a, IntegerType, ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

        input = """a: integer = b[1,2];"""
        expect = """Program([
\tVarDecl(a, IntegerType, ArrayCell(b, [IntegerLit(1), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

        input = """a: integer = b[1+2, false && true];"""
        expect = """Program([
\tVarDecl(a, IntegerType, ArrayCell(b, [BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(&&, BooleanLit(False), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

        input = """a: integer = b[1+2, c[a,b]];"""
        expect = """Program([
\tVarDecl(a, IntegerType, ArrayCell(b, [BinExpr(+, IntegerLit(1), IntegerLit(2)), ArrayCell(c, [Id(a), Id(b)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))




# TEST FULL FORM VARIABLE DECLARATION
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
\tVarDecl(x, IntegerType, IntegerLit(1))
\tVarDecl(y, IntegerType, IntegerLit(2))
\tVarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
\tVarDecl(x, IntegerType, IntegerLit(1))
\tVarDecl(y, IntegerType, IntegerLit(2))
\tVarDecl(z, IntegerType, IntegerLit(3))
\tVarDecl(a, FloatType)
\tVarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

        input = """x: integer = a_x(2);"""
        expect = """Program([
\tVarDecl(x, IntegerType, FuncCall(a_x, [IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

        input = """x: integer = a_x(2,true || false, a[3]);"""
        expect = """Program([
\tVarDecl(x, IntegerType, FuncCall(a_x, [IntegerLit(2), BinExpr(||, BooleanLit(True), BooleanLit(False)), ArrayCell(a, [IntegerLit(3)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

        input = """x, y, z: string = a_x(2), {ac+de, 7.e2}, _9aF("hello");"""
        expect = """Program([
\tVarDecl(x, StringType, FuncCall(a_x, [IntegerLit(2)]))
\tVarDecl(y, StringType, ArrayLit([BinExpr(+, Id(ac), Id(de)), FloatLit(7.e2)]))
\tVarDecl(z, StringType, FuncCall(_9aF, [StringLit(hello)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

        input = """x: integer = a[1+2];"""
        expect = """Program([
\tVarDecl(x, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))




# STATEMENT CHECK
        input = """main: function void () { {} {} }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

        input = """main: function void () { aB = 123; }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(aB), IntegerLit(123))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

        input = """main: function void () { aB = 123; _c9[73] = true; }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(aB), IntegerLit(123)), AssignStmt(ArrayCell(_c9, [IntegerLit(73)]), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

        input = """main: function void () { if ("hi"=="false") c = b; else { a = 2; {}} }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, StringLit(hi), StringLit(false)), AssignStmt(Id(c), Id(b)), BlockStmt([AssignStmt(Id(a), IntegerLit(2)), BlockStmt([])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

        input = """main: function void () { if (12==13) c = b;}"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, IntegerLit(12), IntegerLit(13)), AssignStmt(Id(c), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

        input = """main: function void () { if (12==13) {x, y: float = 1, 2.2; d: string = "?";}}"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, IntegerLit(12), IntegerLit(13)), BlockStmt([VarDecl(x, FloatType, IntegerLit(1)), VarDecl(y, FloatType, FloatLit(2.2)), VarDecl(d, StringType, StringLit(?))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

        input = """main: function void () { x: float = 1;}"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))       

        input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
        main: function void () {
        printInteger(4);
        }"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

        input = """main: function void () {
        printInteger();
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

        input = """main: function void () {
        printInteger(4);
        continue;
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4)), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

        input = """main: function void () {
        if (true) continue;
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

        input = """main: function void () {
        if (true) continue; else break;
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ContinueStmt(), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

        input = """main: function void () {
        if (true) continue; else break;
        return;
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ContinueStmt(), BreakStmt()), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

        input = """main: function void () {
        if (true) continue; else break;
        }
        foo: function integer () {
        return a + c;
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ContinueStmt(), BreakStmt())]))
\tFuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

        input = """foo: function integer () {
        while (a == "hello") {
                if ( b >= 0 ) break;
        }
        }"""
        expect = """Program([
\tFuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), StringLit(hello)), BlockStmt([IfStmt(BinExpr(>=, Id(b), IntegerLit(0)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

        input = """foo: function integer () {
        while (a == "hello") {
                if ( b >= 0 ) break;
        }
        }"""
        expect = """Program([
\tFuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), StringLit(hello)), BlockStmt([IfStmt(BinExpr(>=, Id(b), IntegerLit(0)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

        input = """foo: function integer () {
        x: integer = 0;
        do {
        x = x + 1;
        } while (x < 5);
        }"""
        expect = """Program([
\tFuncDecl(foo, IntegerType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(x), IntegerLit(5)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

        input = """foo: function integer () {
        for (x = 1, x > 0, x + 1){
        print(x); }
        }"""
        expect = """Program([
\tFuncDecl(foo, IntegerType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(>, Id(x), IntegerLit(0)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([CallStmt(print, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

        input = """hi: function void() {
            if(t - 4 == 0) return false;
            }"""
        expect = """Program([
\tFuncDecl(hi, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(-, Id(t), IntegerLit(4)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4]) y = a[4];
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4)])), AssignStmt(Id(y), ArrayCell(a, [IntegerLit(4)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) break;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) break; else x = x - 1;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), BreakStmt(), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) a[4,5] = a[4,5]*2; else x = x - 1;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), AssignStmt(ArrayCell(a, [IntegerLit(4), IntegerLit(5)]), BinExpr(*, ArrayCell(a, [IntegerLit(4), IntegerLit(5)]), IntegerLit(2))), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) x = x + 1; else x = x - 1;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) x = true || false; else x = x - 1;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(x), BinExpr(||, BooleanLit(True), BooleanLit(False))), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) x = true ; else return ;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(x), BooleanLit(True)), ReturnStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) x = true ; else return x;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(x), BooleanLit(True)), ReturnStmt(Id(x)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x = x+1;
                if(y > a[4, 5]) say("saiquai"); else arr[1] = "hi string";
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), CallStmt(say, StringLit(saiquai)), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), StringLit(hi string)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x: array[5] of float;
                x = x+1;
                if(y > a[4, 5]) say(); else arr[1] = "hi string";
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([VarDecl(x, ArrayType([5], FloatType)), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), CallStmt(say, ), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), StringLit(hi string)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

        input = """main: function void() {
            for(x = 5, x <= 12, x*3){
                x: auto = true || false;
                x = x+1;
                if(y > a[4, 5]) break; else arr[1] = "hi string";
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(x), IntegerLit(5)), BinExpr(<=, Id(x), IntegerLit(12)), BinExpr(*, Id(x), IntegerLit(3)), BlockStmt([VarDecl(x, AutoType, BinExpr(||, BooleanLit(True), BooleanLit(False))), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), BreakStmt(), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), StringLit(hi string)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

        input = """main: function void() {
            while(x <= 12){
                x: auto = true || false;
                x = x+1;
                if(y > a[4, 5]) return false && false; else arr[1] = "hi string";
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<=, Id(x), IntegerLit(12)), BlockStmt([VarDecl(x, AutoType, BinExpr(||, BooleanLit(True), BooleanLit(False))), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), IfStmt(BinExpr(>, Id(y), ArrayCell(a, [IntegerLit(4), IntegerLit(5)])), ReturnStmt(BinExpr(&&, BooleanLit(False), BooleanLit(False))), AssignStmt(ArrayCell(arr, [IntegerLit(1)]), StringLit(hi string)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

        input = """main: function void() {
            while(x <= 12){
                x: array[2,3] of string = {"i", "am", "string"};
                x = x+1;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<=, Id(x), IntegerLit(12)), BlockStmt([VarDecl(x, ArrayType([2, 3], StringType), ArrayLit([StringLit(i), StringLit(am), StringLit(string)])), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

        input = """main: function void() {
            while(x <= 12)
                x = !false;
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<=, Id(x), IntegerLit(12)), AssignStmt(Id(x), UnExpr(!, BooleanLit(False))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

        input = """main: function void() { a = {3_72, 5} == "who are you?"; }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(==, ArrayLit([IntegerLit(372), IntegerLit(5)]), StringLit(who are you?)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

        input = """main: function void() { a = {3_72, 5} == "who are you?"; }
        sub: function auto () { calculateX();}"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(==, ArrayLit([IntegerLit(372), IntegerLit(5)]), StringLit(who are you?)))]))
\tFuncDecl(sub, AutoType, [], None, BlockStmt([CallStmt(calculateX, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

        input = """main: function void() { a = {3_72, 5} == "who are you?"; }
        fes: string = "i wanna go";
        sub: function auto () { calculateX();}"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(==, ArrayLit([IntegerLit(372), IntegerLit(5)]), StringLit(who are you?)))]))
\tVarDecl(fes, StringType, StringLit(i wanna go))
\tFuncDecl(sub, AutoType, [], None, BlockStmt([CallStmt(calculateX, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

        input = """main: function void() {
            if(x || 7) say("hello");
            }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(||, Id(x), IntegerLit(7)), CallStmt(say, StringLit(hello)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

        input = """main: function string() {
            if(false) {
                a[5] = a[12] / 12;
                b[9] = b[5] || false;
            }
        }"""
        expect = """Program([
\tFuncDecl(main, StringType, [], None, BlockStmt([IfStmt(BooleanLit(False), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(5)]), BinExpr(/, ArrayCell(a, [IntegerLit(12)]), IntegerLit(12))), AssignStmt(ArrayCell(b, [IntegerLit(9)]), BinExpr(||, ArrayCell(b, [IntegerLit(5)]), BooleanLit(False)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

        input = """main: function string() {
            if(false)
                if (true) a[5] = a[12] / 12;
                else b[9] = b[5] || false;
            else return;
        }"""
        expect = """Program([
\tFuncDecl(main, StringType, [], None, BlockStmt([IfStmt(BooleanLit(False), IfStmt(BooleanLit(True), AssignStmt(ArrayCell(a, [IntegerLit(5)]), BinExpr(/, ArrayCell(a, [IntegerLit(12)]), IntegerLit(12))), AssignStmt(ArrayCell(b, [IntegerLit(9)]), BinExpr(||, ArrayCell(b, [IntegerLit(5)]), BooleanLit(False)))), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

        input = """main: function void() {
            /*
                This is a block comment
            */
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

        input = """rf, aa, aaa: auto = 11*24, qdef(), 15%123;"""
        expect = """Program([
\tVarDecl(rf, AutoType, BinExpr(*, IntegerLit(11), IntegerLit(24)))
\tVarDecl(aa, AutoType, FuncCall(qdef, []))
\tVarDecl(aaa, AutoType, BinExpr(%, IntegerLit(15), IntegerLit(123)))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

        input = """main: function void() {
            /*
                This is a block comment
            */
            // hi line
        }"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

        input = """x: string = 123;
            /*
                This is a block comment
            */"""
        expect = """Program([
\tVarDecl(x, StringType, IntegerLit(123))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

        input = """
            /*
                This is a block comment
            */
            x: string = 123;"""
        expect = """Program([
\tVarDecl(x, StringType, IntegerLit(123))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

        input = """main: function void () {}
            /*
                This is a block comment
            */
            x: string = 123;"""
        expect = """Program([
\tFuncDecl(main, VoidType, [], None, BlockStmt([]))
\tVarDecl(x, StringType, IntegerLit(123))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

        input = """main: function void (param1: string, param2: auto) {}
            x: string = 123;"""
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], None, BlockStmt([]))
\tVarDecl(x, StringType, IntegerLit(123))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        x: string = 123;
        }
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([VarDecl(x, StringType, IntegerLit(123))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        x: string = 123;
        if ( a == b ) print(x);
        }
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([VarDecl(x, StringType, IntegerLit(123)), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(print, Id(x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        x: string = 123;
        if ( a == b ) print(x, "just print");
        }
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([VarDecl(x, StringType, IntegerLit(123)), IfStmt(BinExpr(==, Id(a), Id(b)), CallStmt(print, Id(x), StringLit(just print)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        do { break; } while ( x == 12);
        }
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(12)), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        do { break; } while ( x == 12);
        }
        outer: function string (out paramn: auto) {}
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(12)), BlockStmt([BreakStmt()]))]))
\tFuncDecl(outer, StringType, [OutParam(paramn, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        do { break; } while ( x == 12);
        }
        outer: function string (out paramn: auto) {
        while (fuw == 12.4) {
        return fuw + 12 / 3;
        }
        }
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(12)), BlockStmt([BreakStmt()]))]))
\tFuncDecl(outer, StringType, [OutParam(paramn, AutoType)], None, BlockStmt([WhileStmt(BinExpr(==, Id(fuw), FloatLit(12.4)), BlockStmt([ReturnStmt(BinExpr(+, Id(fuw), BinExpr(/, IntegerLit(12), IntegerLit(3))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        do { break; } while ( x == 12);
        }
        outer: function string (out paramn: auto) {
        while (fuw == 12.4) {
        return fuw + 12 / 3;
        }
        }
        int1: string = "hello int";
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(12)), BlockStmt([BreakStmt()]))]))
\tFuncDecl(outer, StringType, [OutParam(paramn, AutoType)], None, BlockStmt([WhileStmt(BinExpr(==, Id(fuw), FloatLit(12.4)), BlockStmt([ReturnStmt(BinExpr(+, Id(fuw), BinExpr(/, IntegerLit(12), IntegerLit(3))))]))]))
\tVarDecl(int1, StringType, StringLit(hello int))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        do { continue; } while ( !4==3);
        }
        outer: function string (out paramn: auto) {
        while (fuw == 12.4) {
        return true;
        }
        }
        int1: string = "hello int";
        arrayfisrt: array[2,3] of boolean = {{true && false}, {4!=3}};
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([DoWhileStmt(BinExpr(==, UnExpr(!, IntegerLit(4)), IntegerLit(3)), BlockStmt([ContinueStmt()]))]))
\tFuncDecl(outer, StringType, [OutParam(paramn, AutoType)], None, BlockStmt([WhileStmt(BinExpr(==, Id(fuw), FloatLit(12.4)), BlockStmt([ReturnStmt(BooleanLit(True))]))]))
\tVarDecl(int1, StringType, StringLit(hello int))
\tVarDecl(arrayfisrt, ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BinExpr(&&, BooleanLit(True), BooleanLit(False))]), ArrayLit([BinExpr(!=, IntegerLit(4), IntegerLit(3))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

        input = """main: function void (param1: string, param2: auto) inherit sub {
        do { break; } while ( x == 12);
        }
        outer: function string (out paramn: auto) {
        while (fuw == 12.4) {
        return callfunction({1,2},{"a","b"});
        }
        }
        int1: string = "hello int";
        arrayfisrt: array[2,3] of boolean = {true && false, 4!=3};
        """
        expect = """Program([
\tFuncDecl(main, VoidType, [Param(param1, StringType), Param(param2, AutoType)], sub, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(12)), BlockStmt([BreakStmt()]))]))
\tFuncDecl(outer, StringType, [OutParam(paramn, AutoType)], None, BlockStmt([WhileStmt(BinExpr(==, Id(fuw), FloatLit(12.4)), BlockStmt([ReturnStmt(FuncCall(callfunction, [ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([StringLit(a), StringLit(b)])]))]))]))
\tVarDecl(int1, StringType, StringLit(hello int))
\tVarDecl(arrayfisrt, ArrayType([2, 3], BooleanType), ArrayLit([BinExpr(&&, BooleanLit(True), BooleanLit(False)), BinExpr(!=, IntegerLit(4), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))




