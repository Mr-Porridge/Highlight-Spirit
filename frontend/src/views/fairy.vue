<template>
  <div>
    <!--Content-->
    <el-container>
      <!--头部标题-->
      <el-header>Highlight Fairy【C++ 代码高亮】</el-header>
      <!--UI 界面-->
      <el-container>
        <!--左侧代码输入框 st-->
        <el-aside width="50%">
          <!--用户输入组件-->
          <el-input
            type="textarea"
            :autosize="{ minRows: 27, maxRows: 500}"
            placeholder="请输入代码"
            v-model="code"
          >
          </el-input>
        </el-aside>
        <!--左侧代码输入框 ed-->

        <!--右侧代码高亮展示 st-->
        <el-main>
          <div class="grid-content bg-dark" v-html="beauty">
<!--            <span v-for="item in beauty" :class="item.category" v-if="item.value !== '<br>'">{{item.value}}</span>-->
<!--            <span v-else><br/></span>-->
            {{beauty}}
          </div>
        </el-main>
        <!--右侧代码高亮展示 ed-->
      </el-container>
    </el-container>
  </div>

</template>

<script>
  export default {
    name: "fairy",
    data() {
      return {
        code: '',
        opLeft: ['(', '[', '{'],
        opRight: [')', ']', '}'],
        beauty: ''
      }
    },
    methods: {},
    watch: {
      code: function (val, old) {
        console.log(val);
        //自动补全括号 但会出现无法回退的Bug
        // const index = this.opLeft.indexOf(val[val.length - 1]);
        // if (index >= 0) {
        //   this.code += this.opRight[index];
        // }
      }
    }
  }
</script>

<style scoped>
  .bg-dark {
    background: #2F2F2F;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

  .grid-content >>> span {
     margin-left: 1%;
}
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    text-align: center;
  }

  .el-main {
    border-radius: 4px;
    padding: 0;
    margin: 0;
    /*background-color: #E9EEF3;*/
    background-color: #2F2F2F;
  }

.grid-content >>> .sharpe-special {
color: orange;
}

.grid-content >>> .arrow-special {
color: deeppink;
}

.grid-content >>> .word {
color: floralwhite;
}

.grid-content >>> .single-op {
color: deeppink;
}

.grid-content >>> .double-op {
color: deeppink;;
}

.grid-content >>> .string {
color: forestgreen;
}

.grid-content >>> .keyword {
color: darkorchid;
/*color: mediumslateblue;*/
}

.grid-content >>> .separator {
color: floralwhite;
}

.grid-content >>> .number {
color: cornflowerblue;
}

.grid-content >>> .illegal {
color: crimson;
}

.grid-content >>> .comment {
color: gray;
}

.grid-content >>> .escape {
color: chocolate;
}
</style>
