# Generated from D:/Git/labs/Теория языков программирования/Расчётное задание\my_c.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .my_cParser import my_cParser
else:
    from my_cParser import my_cParser

# This class defines a complete generic visitor for a parse tree produced by my_cParser.

class my_cVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by my_cParser#run_program.
    def visitRun_program(self, ctx:my_cParser.Run_programContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#program.
    def visitProgram(self, ctx:my_cParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#data.
    def visitData(self, ctx:my_cParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#typeData.
    def visitTypeData(self, ctx:my_cParser.TypeDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#init.
    def visitInit(self, ctx:my_cParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#main.
    def visitMain(self, ctx:my_cParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#block.
    def visitBlock(self, ctx:my_cParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#blockContent.
    def visitBlockContent(self, ctx:my_cParser.BlockContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#blockItem.
    def visitBlockItem(self, ctx:my_cParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#operator.
    def visitOperator(self, ctx:my_cParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#assignment.
    def visitAssignment(self, ctx:my_cParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#condition.
    def visitCondition(self, ctx:my_cParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#struct.
    def visitStruct(self, ctx:my_cParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#dataStruct.
    def visitDataStruct(self, ctx:my_cParser.DataStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#conditionalOperates.
    def visitConditionalOperates(self, ctx:my_cParser.ConditionalOperatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#shiftOperates.
    def visitShiftOperates(self, ctx:my_cParser.ShiftOperatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#ariphmeticOperates.
    def visitAriphmeticOperates(self, ctx:my_cParser.AriphmeticOperatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#mmdOperates.
    def visitMmdOperates(self, ctx:my_cParser.MmdOperatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#priority_level1.
    def visitPriority_level1(self, ctx:my_cParser.Priority_level1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#priority_level2.
    def visitPriority_level2(self, ctx:my_cParser.Priority_level2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#priority_level3.
    def visitPriority_level3(self, ctx:my_cParser.Priority_level3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#priority_level4.
    def visitPriority_level4(self, ctx:my_cParser.Priority_level4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by my_cParser#elementaryExpression.
    def visitElementaryExpression(self, ctx:my_cParser.ElementaryExpressionContext):
        return self.visitChildren(ctx)



del my_cParser