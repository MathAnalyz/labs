# Generated from D:/Git/labs/Теория языков программирования/Расчётное задание\my_c.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .my_cParser import my_cParser
else:
    from my_cParser import my_cParser

# This class defines a complete listener for a parse tree produced by my_cParser.
class my_cListener(ParseTreeListener):

    # Enter a parse tree produced by my_cParser#run_program.
    def enterRun_program(self, ctx:my_cParser.Run_programContext):
        pass

    # Exit a parse tree produced by my_cParser#run_program.
    def exitRun_program(self, ctx:my_cParser.Run_programContext):
        pass


    # Enter a parse tree produced by my_cParser#program.
    def enterProgram(self, ctx:my_cParser.ProgramContext):
        pass

    # Exit a parse tree produced by my_cParser#program.
    def exitProgram(self, ctx:my_cParser.ProgramContext):
        pass


    # Enter a parse tree produced by my_cParser#data.
    def enterData(self, ctx:my_cParser.DataContext):
        pass

    # Exit a parse tree produced by my_cParser#data.
    def exitData(self, ctx:my_cParser.DataContext):
        pass


    # Enter a parse tree produced by my_cParser#typeData.
    def enterTypeData(self, ctx:my_cParser.TypeDataContext):
        pass

    # Exit a parse tree produced by my_cParser#typeData.
    def exitTypeData(self, ctx:my_cParser.TypeDataContext):
        pass


    # Enter a parse tree produced by my_cParser#init.
    def enterInit(self, ctx:my_cParser.InitContext):
        pass

    # Exit a parse tree produced by my_cParser#init.
    def exitInit(self, ctx:my_cParser.InitContext):
        pass


    # Enter a parse tree produced by my_cParser#main.
    def enterMain(self, ctx:my_cParser.MainContext):
        pass

    # Exit a parse tree produced by my_cParser#main.
    def exitMain(self, ctx:my_cParser.MainContext):
        pass


    # Enter a parse tree produced by my_cParser#block.
    def enterBlock(self, ctx:my_cParser.BlockContext):
        pass

    # Exit a parse tree produced by my_cParser#block.
    def exitBlock(self, ctx:my_cParser.BlockContext):
        pass


    # Enter a parse tree produced by my_cParser#blockContent.
    def enterBlockContent(self, ctx:my_cParser.BlockContentContext):
        pass

    # Exit a parse tree produced by my_cParser#blockContent.
    def exitBlockContent(self, ctx:my_cParser.BlockContentContext):
        pass


    # Enter a parse tree produced by my_cParser#blockItem.
    def enterBlockItem(self, ctx:my_cParser.BlockItemContext):
        pass

    # Exit a parse tree produced by my_cParser#blockItem.
    def exitBlockItem(self, ctx:my_cParser.BlockItemContext):
        pass


    # Enter a parse tree produced by my_cParser#operator.
    def enterOperator(self, ctx:my_cParser.OperatorContext):
        pass

    # Exit a parse tree produced by my_cParser#operator.
    def exitOperator(self, ctx:my_cParser.OperatorContext):
        pass


    # Enter a parse tree produced by my_cParser#assignment.
    def enterAssignment(self, ctx:my_cParser.AssignmentContext):
        pass

    # Exit a parse tree produced by my_cParser#assignment.
    def exitAssignment(self, ctx:my_cParser.AssignmentContext):
        pass


    # Enter a parse tree produced by my_cParser#condition.
    def enterCondition(self, ctx:my_cParser.ConditionContext):
        pass

    # Exit a parse tree produced by my_cParser#condition.
    def exitCondition(self, ctx:my_cParser.ConditionContext):
        pass


    # Enter a parse tree produced by my_cParser#struct.
    def enterStruct(self, ctx:my_cParser.StructContext):
        pass

    # Exit a parse tree produced by my_cParser#struct.
    def exitStruct(self, ctx:my_cParser.StructContext):
        pass


    # Enter a parse tree produced by my_cParser#dataStruct.
    def enterDataStruct(self, ctx:my_cParser.DataStructContext):
        pass

    # Exit a parse tree produced by my_cParser#dataStruct.
    def exitDataStruct(self, ctx:my_cParser.DataStructContext):
        pass


    # Enter a parse tree produced by my_cParser#conditionalOperates.
    def enterConditionalOperates(self, ctx:my_cParser.ConditionalOperatesContext):
        pass

    # Exit a parse tree produced by my_cParser#conditionalOperates.
    def exitConditionalOperates(self, ctx:my_cParser.ConditionalOperatesContext):
        pass


    # Enter a parse tree produced by my_cParser#shiftOperates.
    def enterShiftOperates(self, ctx:my_cParser.ShiftOperatesContext):
        pass

    # Exit a parse tree produced by my_cParser#shiftOperates.
    def exitShiftOperates(self, ctx:my_cParser.ShiftOperatesContext):
        pass


    # Enter a parse tree produced by my_cParser#ariphmeticOperates.
    def enterAriphmeticOperates(self, ctx:my_cParser.AriphmeticOperatesContext):
        pass

    # Exit a parse tree produced by my_cParser#ariphmeticOperates.
    def exitAriphmeticOperates(self, ctx:my_cParser.AriphmeticOperatesContext):
        pass


    # Enter a parse tree produced by my_cParser#mmdOperates.
    def enterMmdOperates(self, ctx:my_cParser.MmdOperatesContext):
        pass

    # Exit a parse tree produced by my_cParser#mmdOperates.
    def exitMmdOperates(self, ctx:my_cParser.MmdOperatesContext):
        pass


    # Enter a parse tree produced by my_cParser#priority_level1.
    def enterPriority_level1(self, ctx:my_cParser.Priority_level1Context):
        pass

    # Exit a parse tree produced by my_cParser#priority_level1.
    def exitPriority_level1(self, ctx:my_cParser.Priority_level1Context):
        pass


    # Enter a parse tree produced by my_cParser#priority_level2.
    def enterPriority_level2(self, ctx:my_cParser.Priority_level2Context):
        pass

    # Exit a parse tree produced by my_cParser#priority_level2.
    def exitPriority_level2(self, ctx:my_cParser.Priority_level2Context):
        pass


    # Enter a parse tree produced by my_cParser#priority_level3.
    def enterPriority_level3(self, ctx:my_cParser.Priority_level3Context):
        pass

    # Exit a parse tree produced by my_cParser#priority_level3.
    def exitPriority_level3(self, ctx:my_cParser.Priority_level3Context):
        pass


    # Enter a parse tree produced by my_cParser#priority_level4.
    def enterPriority_level4(self, ctx:my_cParser.Priority_level4Context):
        pass

    # Exit a parse tree produced by my_cParser#priority_level4.
    def exitPriority_level4(self, ctx:my_cParser.Priority_level4Context):
        pass


    # Enter a parse tree produced by my_cParser#elementaryExpression.
    def enterElementaryExpression(self, ctx:my_cParser.ElementaryExpressionContext):
        pass

    # Exit a parse tree produced by my_cParser#elementaryExpression.
    def exitElementaryExpression(self, ctx:my_cParser.ElementaryExpressionContext):
        pass


