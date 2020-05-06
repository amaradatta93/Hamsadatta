import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import {Observable, from} from 'rxjs';
import { map } from 'rxjs/operators';

import { Category } from '../models/category';
import { Dash } from '../models/dash';

@Injectable({
  providedIn: 'root'
})
export class CategoryviewService {

  constructor(private http: HttpClient) { }

  private categoryUrl = 'http://127.0.0.1:8000/api/user-dashboard/category';

  getCategory(): Observable<Category[]> {
    return this.http.get<Category[]>(this.categoryUrl)
    .pipe(
      map((response: any) => {
        let content = response.categories;
        return content;
      })
    );
  }

  getCategoryPosts(id): Observable<Dash[]> {
    let categoryPostUrl = `http://127.0.0.1:8000/api/user-dashboard/categories/${id}`;
    return this.http.get<Dash[]>(categoryPostUrl)
    .pipe(
      map((response: any) => {
        let content = response.posts;
        return content;
      })
    );
  }
}
