<template>
  <div>
    <!--Content-->
    <el-container>
      <!--头部标题-->
      <el-header>Highlight Fairy【C++ 代码高亮】
        <el-button type="danger" size="mini" class="op-btn" @click="cleanAll">清空</el-button>
        <el-button type="primary" size="mini" class="op-btn" @click="setTemplate">模板</el-button>
        <el-button type="success" size="mini" class="op-btn" @click="open">保存</el-button>
      </el-header>
      <!--UI 界面-->
      <el-container>
        <!--左侧代码输入框 st-->
        <el-aside width="50%">
          <!--用户输入组件-->
          <el-input
            class="a"
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
        temp: '#include <iostream>\n' +
          'using namespace std;\n' +
          'int main() {\n' +
          '\tfloat num = 5.20;\n' +
          '\tcout << "Hello world!\\t" << endl;\n' +
          '\treturn 0;\n' +
          '}',
        opLeft: ['(', '[', '{'],
        opRight: [')', ']', '}'],
        beauty: '',
        userName: '',
      }
    },
    methods: {
      init() {
        let raw = {'code': this.code + "\n"};
        axios({
          method: "post",
          url: "/highlight/",
          data: qs.stringify(raw),
        }).then((res) => {
          this.beauty = res.data;
        }).catch((res) => {
          console.log(res)
        });
      },
      open() {
        this.$prompt('请输入邮箱', 'Highlight Fairy', {
          confirmButtonText: '确认发送',
          cancelButtonText: '容我三思',
          inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
          inputErrorMessage: '邮箱格式不正确'
        }).then(({value}) => {
          this.userName = value;
          this.send();
          this.$message({
            type: 'success',
            message: '已发送至: ' + value
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '取消发送'
          });
        });
      },
      send() {
        let raw = {'user': this.userName, 'content': this.code + "\n"};
        axios({
          method: "post",
          url: "/email/",
          data: qs.stringify(raw),
        }).then((res) => {
          console.log(res);
        }).catch((res) => {
          console.log(res);
        });
      },
      textareaTab() {
        // console.log("e.keyCode");
      },
      cleanAll() {
        this.code = '';
      },
      setTemplate() {
        this.code = this.temp;
      },
      runCode() {
        console.log("Running...")
      }
    },
    watch: {
      code: function (val, old) {
        // console.log(val);
        //自动补全括号 但会出现无法回退的Bug
        // const index = this.opLeft.indexOf(val[val.length - 1]);
        // if (index >= 0) {
        //   this.code += this.opRight[index];
        // }
        // this.code = this.code.replace("  ", "\t"); 改用监听tab
        this.init();
      }
    },
    mounted() {
      this.init();
      // 全局监听键盘事件
      document.onkeydown = function (e) {
        let key = window.event.keyCode; // tab的值为9
        // console.log(event.shiftKey);
        // console.log(key);
        if (key === 9) {
          // 阻止默认事件
          window.event.preventDefault();
          // 获取输入框信息
          let elInput = document.getElementById("userInput");
          let startPos = elInput.selectionStart;
          let endPos = elInput.selectionEnd;
          if (startPos === undefined || endPos === undefined) return;
          let txt = elInput.value;
          // 插入文本
          elInput.value = txt.substring(0, startPos) + "\t" + txt.substring(endPos); // 中间为插入文本
          elInput.focus();
          elInput.selectionStart = startPos + 1; // 插入字符的长度
          elInput.selectionEnd = startPos + 1; // 插入字符的长度
        }
        else if (event.shiftKey && event.keyCode === 57) {
          // 阻止默认事件
          window.event.preventDefault();
          // 获取输入框信息
          let elInput = document.getElementById("userInput");
          let startPos = elInput.selectionStart;
          let endPos = elInput.selectionEnd;
          if (startPos === undefined || endPos === undefined) return;
          let txt = elInput.value;
          // 插入文本
          elInput.value = txt.substring(0, startPos) + "()" + txt.substring(endPos); // 中间为插入文本
          elInput.focus();
          elInput.selectionStart = startPos + 1; // 插入字符的长度
          elInput.selectionEnd = startPos + 1; // 插入字符的长度
        }
        else if (event.shiftKey && key === 219) {
          // 阻止默认事件
          window.event.preventDefault();
          // 获取输入框信息
          let elInput = document.getElementById("userInput");
          let startPos = elInput.selectionStart;
          let endPos = elInput.selectionEnd;
          if (startPos === undefined || endPos === undefined) return;
          let txt = elInput.value;
          // 插入文本
          elInput.value = txt.substring(0, startPos) + "{}" + txt.substring(endPos); // 中间为插入文本
          elInput.focus();
          elInput.selectionStart = startPos + 1; // 插入字符的长度
          elInput.selectionEnd = startPos + 1; // 插入字符的长度
        }
        else if (key === 219) {
          // 阻止默认事件
          window.event.preventDefault();
          // 获取输入框信息
          let elInput = document.getElementById("userInput");
          let startPos = elInput.selectionStart;
          let endPos = elInput.selectionEnd;
          if (startPos === undefined || endPos === undefined) return;
          let txt = elInput.value;
          // 插入文本
          elInput.value = txt.substring(0, startPos) + "[]" + txt.substring(endPos); // 中间为插入文本
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
    margin: 1px 1px 1px 1px;
    background-color: #2F2F2F;
    color: floralwhite;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    text-align: center;
    width: 50%;
  }

  .el-main {
    border-radius: 4px;
    padding: 5px;
    color: white;
    border-top: 1px solid;
    border-right: 1px solid;
    background-color: #2F2F2F;
  }

  .op-btn {
    margin-left: 1%;
  }

  .grid-content >>> .sharpe-special {
    color: orange;
  }

  .grid-content >>> .arrow-special {
    color: turquoise;
  }

  .grid-content >>> .word {
    color: floralwhite;
  }

  .grid-content >>> .single-op {
    color: deeppink;
  }

  .grid-content >>> .double-op {
    color: turquoise;
  }

  .grid-content >>> .string {
    color: forestgreen;
  }

  .grid-content >>> .keyword {
    color: mediumorchid;
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
