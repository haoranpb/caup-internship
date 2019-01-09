<template>
  <div id="txt">
    <el-row type="flex" justify="center">
      <el-col :span="6">
        <div>
          <p>第一步：请选择省份：</p>
          <province-selector />
        </div>
        <div>
          <p>第二步：请选择模型范围大小：</p>
          <size-selector />
        </div>
        <div>
          <p>第三步：请设置风速风向条件：</p>
          <wind-setter />
        </div>
        <div>
          <p>第四步：请选择地况：</p>
          <land-situation />
        </div>
        <div class="button_list">
          <p></p>
          <el-button type="primary" @click="generate">生成文本文件</el-button>
          <el-button type="success" :class="{active: isactive}" @click="download">点击下载文本文件</el-button>
        </div>
      </el-col>
      <el-col :span="6"><div></div></el-col>
    </el-row>
  </div>
</template>

<script>
import ProvinceSelector from '@/components/ProvinceSelector.vue'
import SizeSelector from '@/components/SizeSelector.vue'
import LandSituation from '@/components/LandSituationSelector.vue'
import WindSetter from '@/components/WindSetter'

export default {
  name: 'txt',
  data: function(){
    return {
      isactive: false,
      content: ''
    }
  },
  components: {
    ProvinceSelector,
    SizeSelector,
    LandSituation,
    WindSetter
  },
  methods:{
    generate: function(){
      let location = document.getElementsByClassName('el-cascader__label')[0].textContent.split('/');
      for(let i in location) {
        if(i<2) {
          this.content += location[i].trim() + '/';
        }
        else{
          this.content += location[i].trim() + '\n';
        }
      }
      let textElements = document.getElementsByClassName('el-input__inner');
      this.content += (textElements[1].value + '\n');
      let activeid = document.getElementsByClassName('is-active')[0].id;
      if(activeid == 'tab-first') {
        this.content += (textElements[2].value + '\n');
      }
      else{
        this.content += ('风向：' + textElements[3].value + '\n');
        this.content += ('风速：' + textElements[4].value + '\n');
      }
      this.content += (textElements[5].value + '\n');

      this.isactive = true;
      this.$message({
        message: '生成文本文件成功',
        type: 'success'
      });
    },
    download: function(){
      if(this.isactive) {
        let atag = document.createElement("a");
        let file = new Blob([this.content], {type: 'text/plain'});
        atag.href = URL.createObjectURL(file);
        atag.download = 'result.txt';
        atag.click();
        this.content = '';
      }
      else{
        this.$message.error('请先生成文本文件');
      }
    }
  }
}
</script>

<style>
.button_list {
  margin-top: 40px;
}
</style>
