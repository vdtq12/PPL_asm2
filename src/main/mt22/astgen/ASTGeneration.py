from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
# PROGRAM
    # program: decls EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))
    
    # decls: decl decls | decl ;
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.decl()) + self.visit(ctx.decls())
        else:
            return self.visit(ctx.decl())
        
    # decl: var_decl | func_decl ;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        else:
            return [self.visit(ctx.func_decl())]





# VARIABLE DECLARATION
    # var_decl: (s_var_decl | l_var_decl) SM;
    def visitVar_decl(self, ctx: MT22Parser.Var_declContext):
        if ctx.s_var_decl():
            return self.visit(ctx.s_var_decl())
        else:
            elementList = self.visit(ctx.l_var_decl())
            res = []
            for x in range(int(len(elementList)/2)):
                res += [VarDecl(elementList[x], elementList[int(len(elementList)/2)], elementList[x+int(len(elementList)/2)+1])]
            return res

    # s_var_decl: id_list CM typ;
    def visitS_var_decl(self, ctx: MT22Parser.S_var_declContext):
        idList = self.visit(ctx.id_list())
        res = []
        for i in range(0, len(idList)):
            res += [VarDecl(idList[i], self.visit(ctx.typ()))]
        return res

    # l_var_decl: ID COMMA l_var_decl COMMA (expr|arr_lit) | ID CM typ '=' (expr|arr_lit)
    def visitL_var_decl(self, ctx: MT22Parser.L_var_declContext):
        if ctx.typ():
            return [ctx.ID().getText(), self.visit(ctx.typ()), self.visit(ctx.expr())]
        else:
            return [ctx.ID().getText()] + self.visit(ctx.l_var_decl()) + [self.visit(ctx.expr())]

    # id_list: ID COMMA id_list | ID;
    def visitId_list(self, ctx: MT22Parser.Id_listContext):
        if ctx.getChildCount() == 3:
            return [ctx.ID().getText()] + self.visit(ctx.id_list())
        else:
            return [ctx.ID().getText()]
    
    # typ: INTEGER | FLOAT | STRING | BOOLEAN | AUTO | array_typ;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.AUTO():
            return AutoType()
        else: 
            return self.visit(ctx.array_typ())





# ARRAY TYPE
    # array_typ: ARRAY dimslist OF element_typ;
    def visitArray_typ(self, ctx: MT22Parser.Array_typContext):
        return ArrayType(self.visit(ctx.dimslist()), self.visit(ctx.element_typ()))

    # dimslist: LSB dims RSB;
    def visitDimslist(self, ctx: MT22Parser.DimslistContext):
        return self.visit(ctx.dims())
    
    # dims: INTLIT COMMA dims | INTLIT;
    def visitDims(self, ctx: MT22Parser.DimsContext):
        if ctx.getChildCount() == 3:
            return [ctx.INTLIT().getText()] + self.visit(ctx.dims())
        else:
            return [ctx.INTLIT().getText()]
        
    # element_typ: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitElement_typ(self, ctx: MT22Parser.Element_typContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()





# EXPRESSION
    # expr_list: expr COMMA expr_list | expr;
    def visitExpr_list(self, ctx: MT22Parser.Expr_listContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())
        else:
            return [self.visit(ctx.expr())]
        
    # expr: expr1 SCCOP expr1 | expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1(0))
        
    # expr1: expr2 (EQOP|NEQOP|LTOP|GTOP|LEQOP|GEQOP) expr2 | expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        else:
            return self.visit(ctx.expr2(0))
        
    # expr2: expr2 (ANDOP|OROP) expr3 | expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())
        
    # expr3: expr3 (ADDOP|SUBOP) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())
        
    # expr4: expr4 (MULOP|DIVOP|REMOP) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())
        
    # expr5: NOTOP expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.NOTOP().getText(), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())
        
    # expr6: SUBOP expr6 | expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.SUBOP().getText(), self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())
        
    # expr7: expr7 LSB expr_list RSB | operand;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.expr7().getText(), self.visit(ctx.expr_list()))
        else:
            return self.visit(ctx.operand())
        
    # operand: INTLIT | FLOATLIT | BOOLIT | STRLIT | ID | arr_lit | func_call;
    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.INTLIT():
            return IntegerLit(ctx.getText())
        elif ctx.FLOATLIT():
            return FloatLit(ctx.getText())
        elif ctx.BOOLIT():
            if ctx.getText() == 'true':
                return BooleanLit(True)
            else:
                return BooleanLit(False)
        elif ctx.STRLIT():
            return StringLit(ctx.getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arr_lit(): 
            return ArrayLit(self.visit(ctx.arr_lit()))
        elif ctx.func_call():
            return self.visit(ctx.func_call())





    # idx_oprt: ID LSB expr_list RSB;
    def visitIdx_oprt(self, ctx: MT22Parser.Idx_oprtContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.expr_list()))
    

    # func_call: ID LRB expr_list? RRB;
    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        if ctx.expr_list():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.expr_list()))
        else:
            return FuncCall(ctx.ID().getText(), [])







# ARRAY LITERAL
    # arr_lit: LCB arr_ele_list? RCB;
    def visitArr_lit(self, ctx: MT22Parser.Arr_litContext):
        if ctx.arr_ele_list():
            return self.visit(ctx.arr_ele_list())
        else:
            return []
        
    # arr_ele_list: expr COMMA arr_ele_list | expr;
    def visitArr_ele_list(self, ctx: MT22Parser.Arr_ele_listContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())] + self.visit(ctx.arr_ele_list())
        else:
            return [self.visit(ctx.expr())]





# FUNCTION DECLARATION
    # func_decl: func_proto block_stmt;
    def visitFunc_decl(self, ctx: MT22Parser.Func_declContext):
        protoList = self.visit(ctx.func_proto())
        # print(protoList)
        if protoList.get('inheritID'): 
            if protoList.get('paramList'):
                # print('h1 has param and inherit')
                return FuncDecl(protoList.get('ID'),protoList.get('ret_typ'), protoList.get('paramList'), protoList.get('inheritID'), self.visit(ctx.block_stmt())) #has param and inherit
            # print('h2 has only inherit')
            return FuncDecl(protoList.get('ID'),protoList.get('ret_typ'), [], protoList.get('inheritID'), self.visit(ctx.block_stmt())) #has only inherit
        elif protoList.get('paramList'):
            # print('h3 has only param')
            return FuncDecl(protoList.get('ID'),protoList.get('ret_typ'), protoList.get('paramList'), None, self.visit(ctx.block_stmt())) #has only param
        # print('h4 not have param and inherit')
        return FuncDecl(protoList.get('ID'),protoList.get('ret_typ'), [], None, self.visit(ctx.block_stmt())) #not have param and inherit
    
    # func_proto: ID CM FUNCTION ret_typ LRB param_list? RRB (INHERIT ID)?; 
    def visitFunc_proto(self, ctx: MT22Parser.Func_protoContext):
        inheritRes = ""
        paramRes = []
        if ctx.param_list():
            paramRes = self.visit(ctx.param_list())
        if ctx.INHERIT():
            inheritRes = ctx.ID(1).getText()
        d = {'ID': ctx.ID(0).getText(), 'ret_typ': self.visit(ctx.ret_typ()), 'paramList': paramRes, 'inheritID': inheritRes}
        return d
    
    # ret_typ: VOID | typ;
    def visitRet_typ(self, ctx: MT22Parser.Ret_typContext):
        if ctx.VOID():
            return VoidType()
        else:
            return self.visit(ctx.typ())
        
    # param_list: param COMMA param_list | param;
    def visitParam_list(self, ctx: MT22Parser.Param_listContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.param()) + self.visit(ctx.param_list())
        else:
            return self.visit(ctx.param())

    # param: INHERIT? OUT? ID CM typ;
    def visitParam(self, ctx: MT22Parser.Param_listContext):
        inherit = False
        out = False
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():
            out = True
        return [ParamDecl(ctx.ID().getText(), self.visit(ctx.typ()), out, inherit)]





# STATEMENTS
    # assign_stmt: (ID|idx_oprt) EQUAL expr SM;
    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        if ctx.ID():
            return AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr()))
        else:
            return AssignStmt(self.visit(ctx.idx_oprt()), self.visit(ctx.expr()))
    
    # if_stmt:IF LRB expr RRB stmt (ELSE stmt)?;
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        stmt0 = None
        stmt1 = None
        if isinstance(self.visit(ctx.stmt(0)), Stmt):
            stmt0 = self.visit(ctx.stmt(0))
        if ctx.ELSE():
            if isinstance(self.visit(ctx.stmt(1)), Stmt):
                stmt1 = self.visit(ctx.stmt(1))
            return IfStmt(self.visit(ctx.expr()), stmt0, stmt1)
        else:
            return IfStmt(self.visit(ctx.expr()), stmt0)

    # for_stmt: FOR LRB ID EQUAL expr COMMA expr COMMA expr RRB stmt;
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        stmt = self.visit(ctx.stmt())
        if isinstance(stmt, Stmt):
            pass
        else:
            stmt = None
        return ForStmt(AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr(0))), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), stmt)

    # while_stmt: WHILE LRB expr RRB stmt;
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        stmt = self.visit(ctx.stmt())
        if isinstance(stmt, Stmt):
            pass
        else:
            stmt = None
        return WhileStmt(self.visit(ctx.expr()), stmt)

    # dowhile_stmt: DO block_stmt WHILE LRB expr RRB SM;
    def visitDowhile_stmt(self, ctx: MT22Parser.Dowhile_stmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.block_stmt()))

    # break_stmt: BREAK SM;
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()
    
    # cont_stmt: CONTINUE SM;
    def visitCont_stmt(self, ctx: MT22Parser.Cont_stmtContext):
        return ContinueStmt()

    # return_stmt: RETURN expr? SM;
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        else:
            return ReturnStmt()

    # call_stmt: ID LRB expr_list? RRB SM;
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        if ctx.expr_list():
            return CallStmt(ctx.ID().getText(), self.visit(ctx.expr_list()))
        else:
            return CallStmt(ctx.ID().getText(), [])

    # block_stmt: LCB stmt* RCB;
    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        if ctx.stmt():
            res = []
            for i in range(len(ctx.stmt())):
                temp = self.visit(ctx.stmt(i))
                if isinstance(temp, Stmt):
                    res += [temp]
                else:
                    res += temp
            return BlockStmt(res)
        else:
            return BlockStmt([])

    # stmt: assign_stmt | if_stmt | for_stmt | while_stmt | dowhile_stmt
    # 		| break_stmt | cont_stmt | return_stmt | call_stmt | block_stmt | var_decl ;
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))
    



