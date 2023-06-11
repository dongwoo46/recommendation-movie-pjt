<template>
  <div>
    <p id="what">[친구게시판 상세페이지]</p>
    <div class="board">
      <p class="detailtitle">{{ friendboard?.title }}</p>
      <p class="detailcontent">{{ friendboard?.content }}</p>
      <p>
        작성자 : 
        <router-link class="writer"
          :to="{name: 'ProfileView', params: { username: friendboard?.username }}" style="text-decoration: none">
          {{friendboard?.username}}
        </router-link>
      </p>
      
      <p class="updateat">수정시간 : {{ friendboard?.updated_at.slice(0,10) }} {{ friendboard?.updated_at.slice(11,16) }}</p>
      <router-link :to="{name: 'FriendView'}">
        <button @click="deleteboard">게시물 삭제</button>
      </router-link>
      <br>
      <br>
    </div>
    
    <hr>

    <div>
      <div v-for="(friendcomment, index) in friendcomments" :key="index" >
        <div class="commentboard p-3">
          <div>
          <div class="commentcontent">{{friendcomment.content}}</div>
          <router-link class="writer"
          :to="{name: 'ProfileView', params: { username: friendcomment.user.username }}" style="text-decoration: none">
          {{friendcomment.user.username}}
          </router-link>
        </div>
        <br>
        <p class="updateat">{{friendcomment.updated_at}}</p>
        <button  @click="deleteComment(friendcomment.id)">댓글 삭제</button>
        <br><br>
        </div>
        
      </div>
    </div>
    <br>
    <form @submit.prevent="createComment" @keyup.enter="createComment">
      <div class="form-group">
        <!-- <label for="content">내용:</label> -->
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
    name: 'FriendDetailView',
    data() {
      return {
        newComment: {'content':null,},
        friendboard :null,
        friendcomments : null,
      }
    },
    created(){
      this.getBoards()
    },
    methods: {
      deleteComment(commentId) {
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/articles/friendboard/${this.$route.params.id }/friendcomment/${commentId}/`,
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
          url: `${API_URL}/api/v1/articles/friendboard/${this.$route.params.id }/friendcomment/create/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
          },
          data: this.newComment
        })
        .then(res => {
          this.friendcomments.push(res.data)
          this.newComment.content = '';
        })
        .catch(err=>{
          console.log(err)
        })
      },
      getBoards(){
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/articles/friendboard/${this.$route.params.id }/`,
          headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
        })
        .then((res) => {
          this.friendboard = res.data
          axios({
            method:'get',
            url:`${API_URL}/api/v1/articles/friendboard/${this.$route.params.id }/friendcomment/`,
            headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
          })
          .then(res => {
            this.friendcomments = res.data
          })
        })
        .catch((err) => {
          console.log(err)
        })
        
        
    },
      deleteboard() {
        axios({
          method: 'delete',
          url:`${API_URL}/api/v1/articles/friendboard/${this.$route.params.id }/`,
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