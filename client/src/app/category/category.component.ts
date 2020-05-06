import { Component, OnInit, Output, EventEmitter } from '@angular/core';

import { ActivatedRoute } from '@angular/router';

import { CategoryviewService } from '../services/categoryview.service';
import { Dash } from '../models/dash';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  @Output() categoryPost: Dash[];
  id: any;

  constructor(private categoryviewService: CategoryviewService,
    private activatedRoute: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(params => {
      this.id = params.get('pk');
    this.categoryviewService.getCategoryPosts(this.id)
    .subscribe(categoryPost => this.categoryPost = categoryPost);
    })
  }
  
}
