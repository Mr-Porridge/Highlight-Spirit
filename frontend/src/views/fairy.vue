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
            id="userInput"
            type="textarea"
            :autosize="{ minRows: 27, maxRows: 500}"
            placeholder="请输入代码"
            v-model="code"
            @keyup.tab.native="textareaTab"
          >
          </el-input>
        </el-aside>
        <!--左侧代码输入框 ed-->

        <!--右侧代码高亮展示 st-->
        <el-main>
          <div class="grid-content bg-dark" v-html="beauty"></div>
        </el-main>
        <!--右侧代码高亮展示 ed-->
      </el-container>
    </el-container>
  </div>

</template>

<script>
  import axios from 'axios'
  import qs from 'qs'

  export default {
    name: "fairy",
    data() {
      return {
        code: '#include <iostream>\n' +
          '#define TEST = \'test\'\n' +
          'using namespace std;\n' +
          'int main() {\n' +
          '\tfloat num = 8.78;\n' +
          '\tcout << "Hello world!\\t" << endl;\n' +
          '\treturn 0;\n' +
          '}',
        opLeft: ['(', '[', '{'],
        opRight: [')', ']', '}'],
        beauty: ''
      }
    },
    methods: {
      init() {
        let raw = {'code': this.code + "\n"};
        axios({
          method: "post",
          url: "http://localhost:8000/highlight/",
          data: qs.stringify(raw),
        }).then((res) => {
          this.beauty = res.data;
        }).catch((res) => {
          console.log(res)
        });
      },
      textareaTab() {
        console.log("e.keyCode");
      },
    },
    watch: {
      code: function (val, old) {
        // console.log(val);
        //自动补全括号 但会出现无法回退的Bug
        // const index = this.opLeft.indexOf(val[val.length - 1]);
        // if (index >= 0) {
        //   this.code += this.opRight[index];
        // }
        this.code = this.code.replace("  ", "\t");
        this.init();
      }
    },
    mounted() {
      this.init();
      // 全局监听键盘事件
      document.onkeydown = function (e) {
        let key = window.event.keyCode; // tab的值为9
        if (key === 9) {
          window.event.preventDefault();
          let elInput = document.getElementById("userInput");
          let startPos = elInput.selectionStart;
          let endPos = elInput.selectionEnd;
          if (startPos === undefined || endPos === undefined) return;
          let txt = elInput.value;
          elInput.value = txt.substring(0, startPos) + "\t" + txt.substring(endPos); // 中间为插入文本
          elInput.focus();
          elInput.selectionStart = startPos + 1; // 插入字符的长度
          elInput.selectionEnd = startPos + 1; // 插入字符的长度
        }
      };
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
