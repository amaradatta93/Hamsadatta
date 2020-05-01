import { Component, OnInit } from '@angular/core';

import { Dash } from '../models/dash';
import { DashviewService } from '../services/dashview.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  posts: Dash;

  constructor(private dashviewService: DashviewService) {
  }

  ngOnInit() {
    this.getPosts();
  }

  getPosts(): void {
    this.dashviewService.getPosts()
    .subscribe((posts: any) => this.posts = posts.posts);
  }
  
}
