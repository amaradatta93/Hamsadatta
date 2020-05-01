import { Injectable, Input } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import {Observable} from 'rxjs';

import { map } from 'rxjs/operators';
import { Article } from '../models/article';

@Injectable({
  providedIn: 'root'
})
export class PostviewService {


  constructor(private http: HttpClient) { }
 
  
  getArticle(id: number): Observable<Article> {
    console.log(id);
    let articleUrl = `http://127.0.0.1:8000/api/user-dashboard/posts/${id}`
    return this.http.get<Article>(articleUrl)
    .pipe(
      map((response:any) => {
        let content = response.contents;
       return content;
      })
    )
  }
}
