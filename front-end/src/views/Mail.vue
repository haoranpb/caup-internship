<template>
  <div class="mail">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="邮件主题">
        <el-input v-model="form.title" placeholder="请输入邮箱主题" ></el-input>
      </el-form-item>
      <div>
        <el-upload class="recievers" drag :on-success='displayReciever'
          action="http://ludanxer.top:10000/recievers-upload">
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">请重命名为：reciever.txt！<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传txt文件，每行一个收件邮箱</div>
        </el-upload>
        <div>
          <el-table :data="tableData" stripe height="250" class="recieverTable" style="width: 50%">
            <el-table-column prop="reciever" label="收件人"></el-table-column>
          </el-table>
        </div>
      </div>
      <el-form-item label="邮箱地址">
        <el-input v-model="form.usr" placeholder="xxxxxx@tongji.edu.cn"></el-input>
      </el-form-item>
      <el-form-item label="邮箱密码">
        <el-input v-model="form.pwd" placeholder="请输入邮箱密码" show-password></el-input>
      </el-form-item>
      <el-form-item label="发送间隔">
        <el-input v-model="form.time" placeholder="默认为61，单位秒（s）。请输入纯数字" ></el-input>
      </el-form-item>
      <el-upload class="attachment" drag :on-success='attachmentUpload'
        action="http://ludanxer.top:10000/attachment-upload"
        multiple>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">在此处上传 pdf 附件，<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">只能上传pdf文件</div>
      </el-upload>
      <el-form-item label="邮件正文">
        <el-input autosize type="textarea" v-model="form.content" placeholder="请输入邮件正文"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即发送</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        title: '',
        usr: '',
        pwd: '',
        content: '',
        time: 60
      },
      tableData: [],
      reciever: false,
      attachment: ''
    }
  },
  methods: {
    onSubmit() {
      let obj = this;
      if(this.reciever == false){
        obj.$message.error('请确认上传了reciever.txt');
      }
      else if(this.form.title.length == 0 || this.form.usr.length == 0 || this.form.pwd.length == 0 || this.form.content.length == 0 ){
        obj.$message.error('请确认填好了所有的内容');
      }
      else{
        var params = new URLSearchParams();
        params.append('title', obj.form.title);
        params.append('usr', obj.form.usr);
        params.append('pwd', obj.form.pwd);
        params.append('content', obj.form.content);
        params.append('time', obj.form.time);
        params.append('attachment', obj.attachment);

        obj.$message('开始发送邮件！');
        obj.form = {
          title: '',
          usr: '',
          pwd: '',
          content: '',
          time: 60
        };
        axios({
          method: 'post',
          url: 'http://ludanxer.top:10000/send-mail',
          data: params,
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        })
        .then(function (reponse) {
          console.log(reponse);
        })
        .catch(function () {
          obj.$message.error('糟糕，哪里出了点问题！');
        });
      }
    },
    displayReciever(response){
      this.tableData = [];
      for(let i of response.split('\n')){
        let reciever = [];
        reciever['reciever'] = i;
        this.tableData.push(reciever);
      }
      this.reciever = true;
    },
    attachmentUpload(response){
      this.attachment = response;
    }
  }
}
</script>

<style scoped>
.mail{
  margin-left: 20%;
  margin-right: 20%;
  width: 60%;
}
.recieverTable{
  margin: 2%;
}
.recievers{
  margin-top: 2%;
  margin-bottom: 2%;
  float: left;
  margin-right: 5%;
  width: 40%;
}
.attachment{
  margin: 2%;
}
.content{
  height: 200px;
}
</style>

