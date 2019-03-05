<template>
  <div id="display-2">
    <el-row type="flex" justify="center">
      <el-col :span="6">
        <show-info />
        <h1>2. App 数据</h1>
        <h1>3. 气象站数据</h1>
      </el-col>

    </el-row>

  </div>
</template>

<script>
import ShowInfo from '@/components/ShowInfo.vue'


export default {
  name: 'display-2',
  components: {
    ShowInfo
  }
}
</script>
