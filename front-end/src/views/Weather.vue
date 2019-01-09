<template>
  <div id="weather">
    <el-row type="flex" justify="center">
      <el-col :span="6">
        <show-info />
      </el-col>
      <el-col :span="6">
        <upload-pic />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ShowInfo from '@/components/ShowInfo.vue'
import UploadPic from '@/components/UploadPic.vue'

export default {
  name: 'weather',
  components: {
    ShowInfo,
    UploadPic
  }
}
</script>