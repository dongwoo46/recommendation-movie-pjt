<template>
  <div>
    <p id="what">[연애게시판 상세페이지]</p>
    <div class="board">
      <p class="detailtitle">{{ loveboard?.title }}</p>
      <p class="detailcontent">{{ loveboard?.content }}</p>
      <p>
        작성자 : 
        <router-link class="writer"
          :to="{name: 'ProfileView', params: { username: loveboard?.username }}" style="text-decoration: none">
          {{loveboard?.username}}
        </router-link>
      </p>
      
      <p class="updateat">수정시간 : {{ loveboard?.updated_at.slice(0,10) }} {{ loveboard?.updated_at.slice(11,16) }}</p>
      <router-link :to="{name: 'LoveView'}">
        <button @click="deleteboard">게시물 삭제</button>
      </router-link>
      <br>
      <br>
    </div>
    
    <hr>

    <div>
      <div v-for="(lovecomment, index) in lovecomments" :key="index" >
        <div class="commentboard p-3">
          <div>
          <div class="commentcontent">{{lovecomment.content}}</div>
          <router-link class="writer"
          :to="{name: 'ProfileView', params: { username: lovecomment.user.username }}" style="text-decoration: none">
          {{lovecomment.user.username}}
          </router-link>
        </div>
        <br>
        <p class="updateat">{{ lovecomment.updated_at.slice(0,10) }} {{ lovecomment.updated_at.slice(11,16) }}</p>
        <button  @click="deleteComment(lovecomment.id)">댓글 삭제</button>
        <br><br>
        </div>
        
      </div>
    </div>
    <br>
    <form @submit.prevent="createComment" @keyup.enter="createComment">
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea
          v-model="newComment.content"
          class="form-control"
          id="content"
          rows="3"
          placeholder="댓글을 입력하세요"
          style="text-align: center;"
        ></textarea>
      </div>
      <button @keyup.enter="createComment" type="submit" class="btn btn-primary">댓글 작성</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'LoveDetailView',
    data() {
      return {
        newComment: {'content':null,},
        loveboard :null,
        lovecomments : null,
      }
    },
    created(){
      this.getBoards()
    },
    methods: {
      deleteComment(commentId) {
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/articles/loveboard/${this.$route.params.id }/lovecomment/${commentId}/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
          },
          })
          .then(res => {
            console.log(res)
            this.getBoards()
          })
          .catch(err => {
            console.log(err)
          })

      },
      createComment() {
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/articles/loveboard/${this.$route.params.id }/lovecomment/create/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
          },
          data: this.newComment
        })
        .then(res => {
          this.lovecomments.push(res.data)
          this.newComment.content = '';
        })
        .catch(err=>{
          console.log(err)
        })
      },
      getBoards(){
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/articles/loveboard/${this.$route.params.id }/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        })
        .then((res) => {
          this.loveboard = res.data
          axios({
            method:'get',
            url:`${API_URL}/api/v1/articles/loveboard/${this.$route.params.id }/lovecomment/`,
            headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
          })
          .then(res => {
            this.lovecomments = res.data
          })
        })
        .catch((err) => {
          console.log(err)
        })
        },
      deleteboard() {
        axios({
          method: 'delete',
          url:`${API_URL}/api/v1/articles/loveboard/${this.$route.params.id }/`,
          headers: {
            Authorization: `Token ${ this.$store.state.token }`
          },
          })
          .then(res => {
            console.log(res)
            })
          .catch(err => {
            console.log(err)
            })
            },
    },
    
}
</script>

<style>
.detailtitle{
  color:gold;
  font-family: 'Gugi', cursive;
  font-weight: 10;
  font-size: 70px;
}
.detailcontent{
  color: white;
  font-family: 'IBM Plex Sans KR', sans-serif;
  font-size: 35px;
}
.detailuser{
  color: white;

}
.board{
  border: 1px solid gold;
}

.commentcontent {
  color: white;
  font-family: 'IBM Plex Sans KR', sans-serif;
  font-size: 25px;
}

.writer{
  color: rgb(121, 121, 236);
  font-family: 'Black Han Sans', sans-serif;
  font-size: 15px;
}
.updateat {
  color: rgb(163, 156, 156);
}
.commentboard {
  border: 1px solid white;
}
</style>