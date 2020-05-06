import { Component, OnInit, Output, EventEmitter } from '@angular/core';

import { ActivatedRoute } from '@angular/router';

import { CategoryviewService } from '../services/categoryview.service';
import { Dash } from '../models/dash';

@Component({
  selector: 'app-category',
  templateUrl: '../dashboard/dashboard.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  posts: Dash[];
  id: any;

  constructor(private categoryviewService: CategoryviewService,
    private activatedRoute: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(params => {
      this.id = params.get('pk');
    this.categoryviewService.getCategoryPosts(this.id)
    .subscribe(posts => this.posts = posts);
    })
  }
  
}
