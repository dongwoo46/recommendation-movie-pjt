<template>
  <div v-if="movie">
    <br>
    <div class="d-flex">
      <div>
        <img
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          alt="poster"
          class="borderImg"
        />
      </div>
      <div class="poster-info-space"></div>
      <div class="movie-info">
        <div class="title">
          <div class="d-flex align-items-center justify-content-between">
            <h1 class="movieTitle">
              <b style="font-size: 60px;">{{ movie.title }}</b>
              <!-- <button class="btn btn-black" @click="toggleFavorite"> -->
              <button class="btn btn-black">
                <i class="fas fa-heart" style="color: #ef0606"></i>
              </button>
            </h1>
          </div>
          <br />
        </div>
        <div class="rating" id="voteaverage">
          <p>평점:⭐ {{ movie.vote_average }}</p>
          <br />
        </div>
        <div class="actor-wrapper">
          <div
            v-for="(actor, index) in castList"
            :key="index"
            class="actor-item"
          >
            <div class="actor-info">
              <img
                :src="`https://image.tmdb.org/t/p/w500${actor.profile_path}`"
                alt=""
                class="actorImg"
              />
              <p class="actor-name">{{ actor.name }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="review-section" style="margin-top: 60px;">
      <h2 id="reviewlist" style="color: gold; font-size: 50px;">영화 리뷰</h2>
      <br />
      <p style="color:rgb(241, 105, 105);"> 주의! : 한번 작성한 리뷰는 삭제할 수 없습니다.</p>
      <br>
      <div v-for="review in reviewList" :key="review.id" class="review-item">
        <div class="border border-warning">
          <br>
          <div>
            <router-link id="moviedetailuser"
              :to="{name: 'ProfileView', params: { username: review.user.username }}" style="text-decoration: none;">
              작성자 : {{ review.user.username }}
            </router-link>
          </div>
          <br>
          <p id="reviewcontent">{{ review.content }}</p>
          
          
          <p style="font-size: 15px;">평점 : ⭐{{ review.score }}</p>
          <p class="updateat">
            마지막 수정 날짜 : {{ review.updated_at.slice(0, 10) }}
            {{ review.updated_at.slice(11, 16) }}
          </p>
          <!-- <button @click="reviewDelete">삭제</button> -->
          <br />
        </div>
        <br>
      </div>
      <div v-if="reviewList.length === 0" class="no-reviews">
        댓글이 없습니다.
      </div>
    </div>

    <!-- 댓글 생성 폼 -->
    <form @submit.prevent="createReview">
      <div class="form-group">
        <label for="content">내용:</label>
        <textarea
          v-model="newReview.content"
          class="form-control"
          id="content"
          rows="3"
        ></textarea>
      </div>
      <div class="form-group">
        <label for="author">평점:</label>
        <input
          type="text"
          v-model="newReview.score"
          class="form-control"
          id="score"
        />
      </div>
      <button type="submit" class="btn btn-primary">댓글 작성</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

const API_KEY = process.env.VUE_APP_MOVIE_API_KEY;

export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: null,
      castList: [],
      reviewList: [],
      newReview: { 'content': null, 'score': null },
    };
  },
  methods: {
    movieDetail() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.moviePk}`,
      })
      .then(res => {
        this.movie = res.data
        let movieId = res.data.id


        axios({
          method: 'get',
          url: `https://api.themoviedb.org/3/movie/${movieId}/credits`,
          params: {
          api_key: API_KEY,
          language: 'ko-KR',
        },
        })
        .then(res2 => {
          this.castList = res2.data.cast.slice(0, 8);
        })
        .catch(err => {
          console.log(err)
        })
      })
    },
    toggleFavorite() {
      console.log('구현할 예정')
    },

    reviewListView() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.$route.params.moviePk}/reviews`,
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        },
      })
      .then(res => {
        console.log(res)
        this.reviewList = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },

    createReview() {
      const newReview = this.newReview

        console.log(this.newReview.score);
        if (!(parseInt(this.newReview.score) > 0 && parseInt(this.newReview.score) <= 10)){
          alert('평점은 1~10사이에 값을 입력해주세요')
        }
        else{
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/movies/${this.$route.params.moviePk}/reviews/`,
            data: newReview,
            headers: {
              Authorization: `Token ${ this.$store.state.token }`
              }
              })
              .then(res => {
                this.reviewList.push(res.data);


                this.newReview.content = '';
                this.newReview.score = '';
              })
              .catch(err => {
                console.log('댓글 생성에 실패했습니다.', err);
              })
        }
    },

    // reviewDelete() {
      // axios({
      //   method: 'delete',
      //   url: `http://127.0.0.1:8000/movies/${}/reviews/delete/`,
      //   headers: {
      //     Authorization: `Token ${ this.$store.state.token }`
      //     },
      //     })
      //     .then(res => {
      //       console.log(res)
      //     })
      //     .catch(err => {
      //       console.log(err)
      //     })

    // }
  },

  created() {
    window.scrollTo({
        top: 0,
        // behavior: 'smooth',
      });
    this.movieDetail()
    this.reviewListView()

  },
};
</script>

<style>
img {
  width: 400px;
  height: 550px;
}

.actorImg {
  width: 100px;
  height: 130px;
  border: thick double rgb(250, 252, 130);
}

p {
  color: white;
}

.movie-info {
  text-align: left;
}

#reviewborder{
  border: 1cm;
  border-color: gold;
}

.rating {
  text-align: left;
}

#reviewcontent {
  font-size: 30px;
}

#reviewlist {
  font-family: 'Gugi', cursive;
}

#moviedetailuser{
  font-family: 'Gugi', cursive;
  color: rgb(102, 102, 224);
}

#voteaverage {
  font-family: 'Gugi', cursive;
  font-size: 30px;
}



.actor-wrapper {
  display: flex;
  flex-wrap: wrap;
  font-family: 'Gugi', cursive;
}

.actor-item {
  flex: 0 0 25%;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.actorImg {
  width: 100px;
  height: 130px;
  object-fit: cover;
  /* border-radius: 50%; */
  margin-right: 10px;
}

.poster-info-space {
  width: 20px; /* 원하는 공백의 크기로 조정 */
}

.borderImg {
  border: 2mm ridge gold;
}

.movieTitle {
  color: rgb(255, 201, 85);
  font-size: 50px;
}

.comment-section {
  text-align: left;
}

hr {
  border-color: white;
}

.updateat {
  color: rgb(163, 156, 156);
}
</style>
