<template>
  <div>
    <p id="what">[비밀게시판 상세페이지]</p>
    <div class="board">
      <p class="detailtitle">{{ secretboard?.title }}</p>
      <p class="detailcontent">{{ secretboard?.content }}</p>
      <p class="writer">작성자 : 익명</p>
      <!-- <p>
        작성자 : 
        <router-link class="writer"
          :to="{name: 'ProfileView', params: { username: secretboard?.username }}" style="text-decoration: none">
          {{secretboard?.username}}
        </router-link>
      </p> -->
      
      <p class="updateat">수정시간 :{{ secretboard?.updated_at.slice(0,10) }} {{ secretboard?.updated_at.slice(11,16) }}</p>
      <router-link :to="{name: 'FreeView'}">
        <button @click="deleteboard">게시물 삭제</button>
      </router-link>
      <br>
      <br>
    </div>
    
    <hr>

    <div>
      <div v-for="(secretcomment, index) in secretcomments" :key="index" >
        <div class="commentboard p-3">
          <div>
          <div class="commentcontent">{{secretcomment.content}}</div>
          <br>
          
          <div class="writer">작성자 : 익명</div>
          <!-- <router-link class="writer"
          :to="{name: 'ProfileView', params: { username: secretcomment.user.username }}" style="text-decoration: none">
          {{secretcomment.user.username}}
          </router-link> -->
        </div>
    
        <br>
        <p class="updateat">{{secretcomment.updated_at}}</p>
        <button  @click="deleteComment(secretcomment.id)">댓글 삭제</button>
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
    name: 'SecretDetailView',
    data() {
      return {
        newComment: {'content':null,},
        secretboard :null,
        secretcomments : null,
      }
    },
    created(){
      this.getBoards()
    },
    methods: {
      deleteComment(commentId) {
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/articles/secretboard/${this.$route.params.id }/secretcomment/${commentId}/`,
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
          url: `${API_URL}/api/v1/articles/secretboard/${this.$route.params.id }/secretcomment/create/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
          },
          data: this.newComment
        })
        .then(res => {
          this.secretcomments.push(res.data)
          this.newComment.content = '';
        })
        .catch(err=>{
          console.log(err)
        })
      },
      getBoards(){
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/articles/secretboard/${this.$route.params.id }/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        })
        .then((res) => {
          this.secretboard = res.data
          axios({
            method:'get',
            url:`${API_URL}/api/v1/articles/secretboard/${this.$route.params.id }/secretcomment/`,
            headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
          })
          .then(res => {
            this.secretcomments = res.data
          })
        })
        .catch((err) => {
          console.log(err)
        })
        },

      deleteboard() {
        axios({
          method: 'delete',
          url:`${API_URL}/api/v1/articles/secretboard/${this.$route.params.id }/`,
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