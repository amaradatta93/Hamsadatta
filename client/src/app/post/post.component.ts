import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Article } from '../models/article';
import { PostviewService } from '../services/postview.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {
  blogpost: Article;

  constructor(private postviewService: PostviewService,
    private activatedRoute: ActivatedRoute) {
  }

  ngOnInit() {
    this.activatedRoute.paramMap.subscribe((param: any) => {
      this.postviewService.getArticle(param.params.pk)
        .subscribe(blogpost => this.blogpost = blogpost);
    })
  }
}
