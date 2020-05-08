import { Component, OnInit, Input } from '@angular/core';

import { ActivatedRoute, Router } from '@angular/router';

import { SearchfetchService } from '../services/searchfetch.service';
import { Dash } from '../models/dash';

@Component({
  selector: 'app-search',
  templateUrl: '../dashboard/dashboard.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  search_params: string;
  posts: Dash[] = [];

  constructor(private searchfetchService: SearchfetchService,
    private activatedRoute: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.activatedRoute.queryParams.subscribe((param: any) => {
      this.search_params = param.search_params.replace(/\s+/g, '-').toLowerCase();
      console.log(this.search_params);
      if (this.search_params) {
        this.searchfetchService.getSearchedPosts(this.search_params)
          .subscribe((response: any) => this.posts = response.posts);
      } else {
        this.router.navigateByUrl('dashboard');
      }
    });
  }

}
